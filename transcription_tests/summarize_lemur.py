"""Génération de compte-rendu via AssemblyAI LeMUR (Claude Sonnet).

Utilise transcription_albert.txt d'ETNA_46 comme référence via input_text.

# time python transcription_tests/summarize_lemur.py
"""

import os
import time
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / ".env")

RESULTS_DIR = Path(__file__).parent / "results"
REFERENCE_TRANSCRIPTION = "transcription_albert.txt"

ASSEMBLYAI_HEADERS = {
    "Authorization": os.environ["ASSEMBLYAI_API_KEY"],
    "Content-Type": "application/json",
}

SUMMARY_PROMPT = """Tu es un assistant spécialisé dans la rédaction de comptes rendus de réunion.

À partir de la transcription suivante, rédige un compte rendu structuré en markdown.
Adapte la structure au contenu : inclus uniquement les sections pertinentes parmi :
participants, objet de la réunion, durée estimée, sujets abordés, décisions prises,
questions en suspens, tâches à effectuer (avec responsable si mentionné), prochaine rencontre.

Transcription :
{transcription}"""


def summarize(transcription):
    response = requests.post(
        "https://api.assemblyai.com/lemur/v3/generate/task",
        headers=ASSEMBLYAI_HEADERS,
        json={
            "prompt": SUMMARY_PROMPT.format(transcription=transcription),
            "final_model": "anthropic/claude-sonnet-4-5",
        },
    )
    response.raise_for_status()
    return response.json()["response"]


video_dir = RESULTS_DIR / "ETNA_46"
transcription = (video_dir / "transcription" / REFERENCE_TRANSCRIPTION).read_text(
    encoding="utf-8"
)
summary_dir = video_dir / "summary"
summary_dir.mkdir(exist_ok=True)

summary_path = summary_dir / "summary_lemur.md"
if summary_path.exists():
    print(f"Déjà présent : {summary_path}")
else:
    print("Résumé avec AssemblyAI LeMUR (claude-sonnet-4-5)...")
    t0 = time.time()
    summary = summarize(transcription)
    summary_path.write_text(summary, encoding="utf-8")
    print(f"OK ({time.time() - t0:.1f}s) → {summary_path}")
