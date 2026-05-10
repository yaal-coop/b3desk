"""Génération de compte-rendu via Groq LLM (llama-3.3-70b-versatile).

Utilise transcription_albert.txt d'ETNA_46 comme référence.

# time python transcription_tests/summarize_groq.py
"""

import os
import time
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(Path(__file__).parent / ".env")

RESULTS_DIR = Path(__file__).parent / "results"
REFERENCE_TRANSCRIPTION = "transcription_albert.txt"
MODEL = "llama-3.1-8b-instant"

SUMMARY_PROMPT = """Tu es un assistant spécialisé dans la rédaction de comptes rendus de réunion.

À partir de la transcription suivante, rédige un compte rendu structuré en markdown.
Adapte la structure au contenu : inclus uniquement les sections pertinentes parmi :
participants, objet de la réunion, durée estimée, sujets abordés, décisions prises,
questions en suspens, tâches à effectuer (avec responsable si mentionné), prochaine rencontre.

Transcription :
{transcription}"""

groq = OpenAI(
    api_key=os.environ["GROQ_API_KEY"],
    base_url="https://api.groq.com/openai/v1",
)


def summarize(transcription):
    response = groq.chat.completions.create(
        model=MODEL,
        temperature=0.3,
        messages=[
            {
                "role": "user",
                "content": SUMMARY_PROMPT.format(transcription=transcription),
            }
        ],
    )
    return response.choices[0].message.content


video_dir = RESULTS_DIR / "ETNA_46"
transcription = (video_dir / "transcription" / REFERENCE_TRANSCRIPTION).read_text(
    encoding="utf-8"
)
summary_dir = video_dir / "summary"
summary_dir.mkdir(exist_ok=True)

summary_path = summary_dir / "summary_groq_llama_8b.md"
if summary_path.exists():
    print(f"Déjà présent : {summary_path}")
else:
    print(f"Résumé avec {MODEL}...")
    t0 = time.time()
    summary = summarize(transcription)
    summary_path.write_text(summary, encoding="utf-8")
    print(f"OK ({time.time() - t0:.1f}s) → {summary_path}")
