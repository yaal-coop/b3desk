"""Transcription via Speechmatics + résumé via Albert API."""
# time python transcription_tests/speechmatics.py

import json
import os
import time
from pathlib import Path

import requests
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(Path(__file__).parent / ".env")

AUDIO_DIR = Path(__file__).parent / "audio"
RESULTS_DIR = Path(__file__).parent / "results"

SPEECHMATICS_BASE_URL = "https://asr.api.speechmatics.com/v2"
SPEECHMATICS_HEADERS = {"Authorization": f"Bearer {os.environ['SPEECHMATICS_API_KEY']}"}
SPEECHMATICS_CONFIG = json.dumps(
    {
        "type": "transcription",
        "transcription_config": {"language": "fr", "operating_point": "enhanced"},
    }
)

SUMMARY_MODEL = "openai/gpt-oss-120b"
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


def submit_job(audio_path):
    with open(audio_path, "rb") as f:
        response = requests.post(
            f"{SPEECHMATICS_BASE_URL}/jobs/",
            headers=SPEECHMATICS_HEADERS,
            files={"data_file": f, "config": (None, SPEECHMATICS_CONFIG)},
        )
    if not response.ok:
        raise RuntimeError(
            f"Speechmatics error {response.status_code}: {response.text}"
        )
    return response.json()["id"]


def poll(job_id, interval=10):
    while True:
        response = requests.get(
            f"{SPEECHMATICS_BASE_URL}/jobs/{job_id}",
            headers=SPEECHMATICS_HEADERS,
        )
        response.raise_for_status()
        status = response.json()["job"]["status"]
        print(f"  statut : {status}")
        if status == "done":
            return
        if status in ("rejected", "expired"):
            raise RuntimeError(f"Job {job_id} échoué : {status}")
        time.sleep(interval)


def get_transcript(job_id):
    response = requests.get(
        f"{SPEECHMATICS_BASE_URL}/jobs/{job_id}/transcript",
        headers=SPEECHMATICS_HEADERS,
        params={"format": "txt"},
    )
    response.raise_for_status()
    response.encoding = "utf-8"
    return response.text


def summarize(transcription):
    response = albert.chat.completions.create(
        model=SUMMARY_MODEL,
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
        transcription_dir, "transcription_speechmatics", "txt"
    )
    summary_path = next_run_path(summary_dir, "summary_speechmatics", "md")

    print(f"\n[{name}] soumission du job...")
    t0 = time.time()
    job_id = submit_job(audio_path)
    print(f"[{name}] job {job_id}, attente des résultats...")
    poll(job_id)
    transcription = get_transcript(job_id)
    transcription_path.write_text(transcription, encoding="utf-8")
    print(f"[{name}] transcription OK ({time.time() - t0:.1f}s) → {transcription_path}")

    print(f"[{name}] résumé...")
    t0 = time.time()
    summary = summarize(transcription)
    summary_path.write_text(summary, encoding="utf-8")
    print(f"[{name}] résumé OK ({time.time() - t0:.1f}s) → {summary_path}")


for audio_file in sorted(AUDIO_DIR.glob("*.mp3")):
    if "_extrait" not in audio_file.name and "ETNA_46" not in audio_file.name:
        process(audio_file)
