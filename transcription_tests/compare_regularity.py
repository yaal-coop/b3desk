"""Comparaison de la régularité des transcriptions : similarité entre les versions d'un même outil."""

from difflib import SequenceMatcher
from pathlib import Path

RESULTS_DIR = Path(__file__).parent / "results"
VIDEOS = ["ETNA_46", "Reunion_Git_YAAL", "video_0"]
TOOLS = [
    "albert",
    "assemblyai",
    "deepgram",
    "gladia",
    "groq",
    "pyannote",
    "revai",
    "speechmatics",
]


def load_versions(video, tool):
    """Retourne la liste des transcriptions disponibles pour cet outil, triées par version."""
    d = RESULTS_DIR / video / "transcription"
    files = []
    base = d / f"transcription_{tool}.txt"
    if base.exists():
        files.append(base)
    for p in sorted(d.glob(f"transcription_{tool}_*.txt")):
        if p.stem.rsplit("_", 1)[-1].isdigit():
            files.append(p)
    return files


def similarity(text_a, text_b):
    """Similarité mot à mot entre deux textes (0.0 à 1.0)."""
    words_a = text_a.lower().split()
    words_b = text_b.lower().split()
    return SequenceMatcher(None, words_a, words_b).ratio()


def word_count(text):
    return len(text.split())


rows = []

for video in VIDEOS:
    for tool in TOOLS:
        versions = load_versions(video, tool)
        if len(versions) < 2:
            continue
        texts = [p.read_text(encoding="utf-8").strip() for p in versions]
        pairs = [(texts[i], texts[i + 1]) for i in range(len(texts) - 1)]
        scores = [similarity(a, b) for a, b in pairs]
        rows.append(
            {
                "video": video,
                "outil": tool,
                "versions": len(versions),
                "scores": scores,
                "mots_v1": word_count(texts[0]),
            }
        )

# Affichage
col_video = 20
col_outil = 14
col_scores = 36
col_mots = 10

header = f"{'Vidéo':<{col_video}} {'Outil':<{col_outil}} {'Versions':<10} {'Similarité':<{col_scores}} {'Mots v1':<{col_mots}}"
print(header)
print("-" * len(header))

for r in rows:
    score_str = "  ".join(
        f"v{i + 1}↔v{i + 2}: {s * 100:.1f}%" for i, s in enumerate(r["scores"])
    )
    print(
        f"{r['video']:<{col_video}} {r['outil']:<{col_outil}} {r['versions']:<10} {score_str:<{col_scores}} {r['mots_v1']:<{col_mots}}"
    )
