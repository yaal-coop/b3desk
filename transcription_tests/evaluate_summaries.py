"""Évaluation comparative des résumés A–J par gpt-4o (tiers neutre).

Deux appels pour contourner la limite TPM de 30 000 tokens/requête :
1. Extraction des points clés de la transcription
2. Évaluation comparative sur 4 critères : fiabilité, hallucinations, pertinence, qualité synthétique
"""

import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(Path(__file__).parent / ".env")

BASE = Path(__file__).parent / "results/ETNA_46"
TRANSCRIPTION = BASE / "transcription/transcription_albert.txt"
SUMMARIES_DIR = BASE / "summary"
OUTPUT = BASE / "evaluation_gpt4o_v3.md"

SUMMARIES = [
    ("A", "summary_albert_v3.md"),
    ("B", "summary_mistral_small_v3.md"),
    ("C", "summary_ministral_3b_v3.md"),
    ("D", "summary_qwen3_coder_v3.md"),
    ("E", "summary_gpt4o_mini_v3.md"),
    ("F", "summary_gpt4o_v3.md"),
    ("G", "summary_claude_haiku_v3.md"),
    ("H", "summary_claude_sonnet_v3.md"),
    ("I", "summary_mistral_small_mistral_api_v3.md"),
    ("J", "summary_mistral_large_mistral_api_v3.md"),
]

KEYPOINTS_PROMPT = """Voici la transcription d'une réunion de projet.

Extrais une liste numérotée et exhaustive de tous les faits vérifiables présents dans la transcription :
chiffres exacts, noms de personnes, noms de projets ou outils, décisions prises, dates ou délais mentionnés, tâches attribuées avec responsable.

Format : une ligne par fait, courte et factuelle. Ne commente pas, ne synthétise pas.

Transcription :
{transcription}"""

EVAL_PROMPT = """Tu vas évaluer et comparer 10 comptes rendus de réunion (A à J) sur 4 critères.

## Critères d'évaluation

1. **Fiabilité** (1–5) : les informations présentes sont-elles exactes ? (chiffres, dates, noms, responsables)
2. **Hallucinations** (1–5) : le résumé est-il exempt d'informations absentes de la transcription ? (5 = aucune hallucination)
3. **Pertinence** (1–5) : les points importants de la réunion sont-ils couverts ?
4. **Qualité synthétique** (1–5) : le résumé est-il clair, concis et bien structuré ?

## Instructions

Pour chaque résumé (A à J), dans cet ordre :
- Note chaque critère de 1 à 5
- Justifie chaque note en 1 ligne
- Si une hallucination est détectée, cite-la exactement entre guillemets

À la fin, produis un tableau récapitulatif (colonnes : Résumé, Fiabilité, Hallucinations, Pertinence, Qualité synthétique, Total/20) et un classement des 3 meilleurs.

Réponds directement en markdown, sans encapsuler dans un bloc de code.

## Faits de référence extraits de la transcription
{keypoints}

## Résumés à évaluer
{summaries}"""


client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

# Étape 1 : extraction des points clés
transcription = TRANSCRIPTION.read_text(encoding="utf-8")
print("Étape 1 : extraction des points clés...")
r1 = client.chat.completions.create(
    model="gpt-4o",
    temperature=0,
    messages=[
        {
            "role": "user",
            "content": KEYPOINTS_PROMPT.format(transcription=transcription),
        }
    ],
)
keypoints = r1.choices[0].message.content
print(f"  {r1.usage.total_tokens} tokens utilisés")

# Étape 2 : évaluation des résumés
summaries_text = "\n\n---\n\n".join(
    f"### Résumé {ref}\n\n"
    + (SUMMARIES_DIR / filename).read_text(encoding="utf-8").strip()
    for ref, filename in SUMMARIES
)
print("Étape 2 : évaluation des résumés...")
r2 = client.chat.completions.create(
    model="gpt-4o",
    temperature=0,
    messages=[
        {
            "role": "user",
            "content": EVAL_PROMPT.format(
                keypoints=keypoints, summaries=summaries_text
            ),
        }
    ],
)
result = r2.choices[0].message.content
print(f"  {r2.usage.total_tokens} tokens utilisés")

OUTPUT.write_text(
    f"# Évaluation comparative des résumés A–J par gpt-4o (v3)\n\n## Points clés de référence\n\n{keypoints}\n\n---\n\n## Évaluation\n\n{result}",
    encoding="utf-8",
)
print(f"Résultat écrit → {OUTPUT}")
