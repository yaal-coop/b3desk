"""Extract mono MP3 audio from meeting videos for transcription tests."""

import subprocess
from pathlib import Path

VIDEOS = {
    "video_0": Path(
        "/home/sebastien/Nextcloud/Sbir Folder/NOTES/Donnees_reelles_test_IA/video_0.mp4"
    ),
    "ETNA_46": Path(
        "/home/sebastien/Nextcloud/Sbir Folder/NOTES/Donnees_reelles_test_IA/ETNA/ETNA_46.mp4"
    ),
    "Reunion_Git_YAAL": Path(
        "/home/sebastien/Nextcloud/Sbir Folder/NOTES/Donnees_reelles_test_IA/Reunion_Git_YAAL/Reunion_Git_YAAL.mp4"
    ),
    "video_0_extrait": Path(
        "/home/sebastien/Nextcloud/Sbir Folder/NOTES/Donnees_reelles_test_IA/video_0_extrait.mp4"
    ),
    "ETNA_46_extrait": Path(
        "/home/sebastien/Nextcloud/Sbir Folder/NOTES/Donnees_reelles_test_IA/ETNA/ETNA_46_extrait.mp4"
    ),
    "ETNA_46_extrait2": Path(
        "/home/sebastien/Nextcloud/Sbir Folder/NOTES/Donnees_reelles_test_IA/ETNA/ETNA_46_extrait2.mp4"
    ),
}

OUTPUT_DIR = Path(__file__).parent / "audio"


def extract(name, video_path):
    output = OUTPUT_DIR / f"{name}.mp3"
    if output.exists():
        print(f"[{name}] déjà extrait, on passe.")
        return
    print(f"[{name}] extraction en cours...")
    subprocess.run(
        [
            "ffmpeg",
            "-i",
            str(video_path),
            "-vn",
            "-ac",
            "1",
            "-ar",
            "16000",
            "-b:a",
            "32k",
            str(output),
        ],
        check=True,
    )
    size_mb = output.stat().st_size / 1_000_000
    print(f"[{name}] OK — {size_mb:.1f} MB")


for name, path in VIDEOS.items():
    extract(name, path)
