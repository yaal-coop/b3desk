"""Transcription via pyannote.ai + résumé via Albert API."""
# uv pip install -r transcription_tests/requirements.txt
# time python transcription_tests/pyannote_ai.py

import os
import time
from pathlib import Path

import requests
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(Path(__file__).parent / ".env")

AUDIO_DIR = Path(__file__).parent / "audio"
RESULTS_DIR = Path(__file__).parent / "results"

PYANNOTE_API_KEY = os.environ["PYANNOTE_API_KEY"]
PYANNOTE_BASE_URL = "https://api.pyannote.ai/v1"
PYANNOTE_HEADERS = {"Authorization": f"Bearer {PYANNOTE_API_KEY}"}

ALBERT_SUMMARY_MODEL = "openai/gpt-oss-120b"
SUMMARY_PROMPT = """Tu es un assistant spécialisé dans la rédaction de comptes rendus de réunion.

À partir de la transcription suivante, rédige un compte rendu structuré en markdown.
Adapte la structure au contenu : inclus uniquement les sections pertinentes parmi :
participants, objet de la réunion, durée estimée, sujets abordés, décisions prises,
questions en suspens, tâches à effectuer (avec responsable si mentionné), prochaine rencontre.

Transcription :
{transcription}"""

albert = OpenAI(
    api_key=os.environ["ALBERT_API_KEY"],
    base_url="https://albert.api.etalab.gouv.fr/v1",
)


def upload(audio_path, media_key, retries=3):
    """Upload le fichier audio vers le stockage pyannote.ai."""
    data = audio_path.read_bytes()
    for attempt in range(1, retries + 1):
        response = requests.post(
            f"{PYANNOTE_BASE_URL}/media/input",
            json={"url": f"media://{media_key}"},
            headers=PYANNOTE_HEADERS,
        )
        response.raise_for_status()
        presigned_url = response.json()["url"]
        try:
            # verify=False : contournement incompatibilité TLS Python 3.14 / S3 AWS
            put_response = requests.put(
                presigned_url, data=data, verify=False, timeout=60
            )
            put_response.raise_for_status()
            return
        except Exception as e:
            if attempt == retries:
                raise
            print(
                f"  upload échoué (tentative {attempt}/{retries}) : {e}, on réessaie..."
            )


def submit_job(media_key):
    """Soumet un job de transcription."""
    response = requests.post(
        f"{PYANNOTE_BASE_URL}/diarize",
        json={
            "url": f"media://{media_key}",
            "transcription": True,
        },
        headers=PYANNOTE_HEADERS,
    )
    response.raise_for_status()
    return response.json()["jobId"]


def poll(job_id, interval=15):
    """Attend la fin du job et retourne le résultat."""
    while True:
        response = requests.get(
            f"{PYANNOTE_BASE_URL}/jobs/{job_id}",
            headers=PYANNOTE_HEADERS,
        )
        response.raise_for_status()
        data = response.json()
        status = data["status"]
        print(f"  statut : {status}")
        if status == "succeeded":
            return data["output"]
        if status == "failed":
            raise RuntimeError(f"Job {job_id} échoué : {data}")
        time.sleep(interval)


def extract_text(output):
    """Concatène les segments de transcription en texte brut."""
    segments = output.get("turnLevelTranscription", [])
    return " ".join(seg["text"].strip() for seg in segments if seg.get("text"))


def summarize(transcription):
    response = albert.chat.completions.create(
        model=ALBERT_SUMMARY_MODEL,
        temperature=0.3,
        messages=[
            {
                "role": "user",
                "content": SUMMARY_PROMPT.format(transcription=transcription),
            }
        ],
    )
    return response.choices[0].message.content


def next_run_path(directory, stem, suffix):
    existing = list(directory.glob(f"{stem}_*.{suffix}"))
    n = max(
        (
            int(p.stem.rsplit("_", 1)[-1])
            for p in existing
            if p.stem.rsplit("_", 1)[-1].isdigit()
        ),
        default=0,
    )
    return directory / f"{stem}_{n + 1}.{suffix}"


def process(audio_path):
    name = audio_path.stem
    transcription_dir = RESULTS_DIR / name / "transcription"
    summary_dir = RESULTS_DIR / name / "summary"
    transcription_dir.mkdir(parents=True, exist_ok=True)
    summary_dir.mkdir(parents=True, exist_ok=True)

    transcription_path = next_run_path(
        transcription_dir, "transcription_pyannote", "txt"
    )
    summary_path = next_run_path(summary_dir, "summary_pyannote", "md")

    print(f"\n[{name}] upload + transcription...")
    t0 = time.time()
    upload(audio_path, name)
    job_id = submit_job(name)
    print(f"[{name}] job {job_id}, attente des résultats...")
    output = poll(job_id)

    import json

    (transcription_dir / "output_raw.json").write_text(
        json.dumps(output, indent=2, ensure_ascii=False)
    )

    transcription = extract_text(output)
    transcription_path.write_text(transcription, encoding="utf-8")
    print(f"[{name}] transcription OK ({time.time() - t0:.1f}s) → {transcription_path}")

    print(f"[{name}] résumé via Albert...")
    t0 = time.time()
    summary = summarize(transcription)
    summary_path.write_text(summary, encoding="utf-8")
    print(f"[{name}] résumé OK ({time.time() - t0:.1f}s) → {summary_path}")


for audio_file in sorted(AUDIO_DIR.glob("*_extrait*.mp3")):
    process(audio_file)
