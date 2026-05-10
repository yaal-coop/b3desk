"""Génération de comptes-rendus via les modèles LLM disponibles sur Albert (DINUM).

Utilise transcription_albert.txt d'ETNA_46 comme référence.
Les résumés déjà présents sont ignorés (relance idempotente).

# time python transcription_tests/summarize_albert.py
"""

import os
import time
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(Path(__file__).parent / ".env")

RESULTS_DIR = Path(__file__).parent / "results"
REFERENCE_TRANSCRIPTION = "transcription_albert.txt"

MODELS = [
    ("albert", "openai/gpt-oss-120b"),
    ("mistral_small", "mistralai/Mistral-Small-3.2-24B-Instruct-2506"),
    ("ministral_3b", "mistralai/Ministral-3-8B-Instruct-2512"),
    ("qwen3_coder", "Qwen/Qwen3-Coder-30B-A3B-Instruct"),
]

SUMMARY_PROMPT = """Tu es un assistant spécialisé dans la rédaction de comptes rendus de réunion.

À partir de la transcription ci-dessous, rédige un compte rendu en markdown avec exactement ces sections (dans cet ordre, uniquement si le contenu est présent) :
- Participants
- Objet de la réunion
- Sujets abordés
- Décisions prises
- Questions en suspens
- Tâches à effectuer (responsable si mentionné)
- Prochaine rencontre

Règles strictes :
- N'inclus que des informations explicitement présentes dans la transcription.
- N'invente aucun chiffre, date, nom ou durée absent de la transcription.
- Si une information est incertaine ou mal audible, ne l'inclus pas.
- Réponds directement en markdown, sans encapsuler dans un bloc de code.

Transcription :
{transcription}"""

albert = OpenAI(
    api_key=os.environ["ALBERT_API_KEY"],
    base_url="https://albert.api.etalab.gouv.fr/v1",
)


def summarize(transcription, model):
    response = albert.chat.completions.create(
        model=model,
        temperature=0.3,
        messages=[
            {
                "role": "user",
                "content": SUMMARY_PROMPT.format(transcription=transcription),
            }
        ],
    )
    return response.choices[0].message.content


for video_dir in [RESULTS_DIR / "ETNA_46"]:
    transcription_path = video_dir / "transcription" / REFERENCE_TRANSCRIPTION
    if not transcription_path.exists():
        continue

    transcription = transcription_path.read_text(encoding="utf-8")
    summary_dir = video_dir / "summary"
    summary_dir.mkdir(exist_ok=True)

    for slug, model in MODELS:
        summary_path = summary_dir / f"summary_{slug}_v3.md"
        if summary_path.exists():
            print(f"[{video_dir.name}] {slug} — déjà présent, ignoré")
            continue

        print(f"\n[{video_dir.name}] résumé avec {model}...")
        t0 = time.time()
        summary = summarize(transcription, model)
        summary_path.write_text(summary, encoding="utf-8")
        print(f"[{video_dir.name}] OK ({time.time() - t0:.1f}s) → {summary_path}")
