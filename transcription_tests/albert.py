"""Transcription + résumé via Albert API (DINUM)."""
# uv pip install -r transcription_tests/requirements.txt
# time python transcription_tests/albert.py

import os
import time
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(Path(__file__).parent / ".env")

AUDIO_DIR = Path(__file__).parent / "audio"
RESULTS_DIR = Path(__file__).parent / "results"

TRANSCRIPTION_MODEL = "openai/whisper-large-v3"
SUMMARY_MODEL = "openai/gpt-oss-120b"

SUMMARY_PROMPT = """Tu es un assistant spécialisé dans la rédaction de comptes rendus de réunion.

À partir de la transcription suivante, rédige un compte rendu structuré en markdown.
Adapte la structure au contenu : inclus uniquement les sections pertinentes parmi :
participants, objet de la réunion, durée estimée, sujets abordés, décisions prises,
questions en suspens, tâches à effectuer (avec responsable si mentionné), prochaine rencontre.

Transcription :
{transcription}"""

client = OpenAI(
    api_key=os.environ["ALBERT_API_KEY"],
    base_url="https://albert.api.etalab.gouv.fr/v1",
)


def transcribe(audio_path):
    with open(audio_path, "rb") as f:
        response = client.audio.transcriptions.create(
            model=TRANSCRIPTION_MODEL,
            file=f,
            language="fr",
        )
    return response.text


def summarize(transcription):
    response = client.chat.completions.create(
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

    transcription_path = next_run_path(transcription_dir, "transcription_albert", "txt")
    summary_path = next_run_path(summary_dir, "summary_albert", "md")

    print(f"\n[{name}] transcription...")
    t0 = time.time()
    transcription = transcribe(audio_path)
    transcription_path.write_text(transcription, encoding="utf-8")
    print(f"[{name}] transcription OK ({time.time() - t0:.1f}s) → {transcription_path}")

    print(f"[{name}] résumé...")
    t0 = time.time()
    summary = summarize(transcription)
    summary_path.write_text(summary, encoding="utf-8")
    print(f"[{name}] résumé OK ({time.time() - t0:.1f}s) → {summary_path}")


for audio_file in sorted(AUDIO_DIR.glob("*_extrait*.mp3")):
    process(audio_file)
