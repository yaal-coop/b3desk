"""Génération de comptes-rendus via Anthropic Claude.

Utilise transcription_albert.txt d'ETNA_46 comme référence.
Les résumés déjà présents sont ignorés (relance idempotente).

# time python transcription_tests/summarize_claude.py
"""

import os
import time
from pathlib import Path

import anthropic
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / ".env")

RESULTS_DIR = Path(__file__).parent / "results"
REFERENCE_TRANSCRIPTION = "transcription_albert.txt"

MODELS = [
    ("claude_haiku", "claude-haiku-4-5-20251001"),
    ("claude_sonnet", "claude-sonnet-4-6"),
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

client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])


def summarize(transcription, model):
    message = client.messages.create(
        model=model,
        max_tokens=4096,
        temperature=0.3,
        messages=[
            {
                "role": "user",
                "content": SUMMARY_PROMPT.format(transcription=transcription),
            }
        ],
    )
    return message.content[0].text


video_dir = RESULTS_DIR / "ETNA_46"
transcription = (video_dir / "transcription" / REFERENCE_TRANSCRIPTION).read_text(
    encoding="utf-8"
)
summary_dir = video_dir / "summary"
summary_dir.mkdir(exist_ok=True)

for slug, model in MODELS:
    summary_path = summary_dir / f"summary_{slug}_v3.md"
    if summary_path.exists():
        print(f"{slug} — déjà présent, ignoré")
        continue

    print(f"Résumé avec {model}...")
    t0 = time.time()
    summary = summarize(transcription, model)
    summary_path.write_text(summary, encoding="utf-8")
    print(f"OK ({time.time() - t0:.1f}s) → {summary_path}")
