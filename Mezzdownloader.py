import os
import yt_dlp
from colorama import Fore, init

init(autoreset=True)

RED = Fore.RED
GREEN = Fore.GREEN
WHITE = Fore.WHITE


def download():
    print(WHITE +"||=============================================||")
    print(WHITE +"||               Mezz Downloader               ||")
    print(WHITE +"||                   by Mezz                   ||")
    print(WHITE +"||=============================================||")

    print()
    print()

    url = input(
        WHITE + "Rentre l'URL de la vidéo que tu veux télécharger : "
    ).strip()

    output_dir = input(
        WHITE + "Dossier de destination où la vidéo va se trouver : "
    ).strip()

    while not os.path.isdir(output_dir):
        print(f"{RED}[!] Le dossier n'existe pas.")
        output_dir = input(
            WHITE + "Dossier de destination : "
        ).strip()

    mp3 = input(
        WHITE + "Tu veux télécharger en MP3 ? (oui/non) : "
    ).strip().lower()

    if mp3 == "oui":
        options = {
            "format": "bestaudio/best",
            "outtmpl": os.path.join(
                output_dir,
                "%(title)s.%(ext)s"
            ),
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
        }
    else:
        options = {
            "format": "bestvideo+bestaudio/best",
            "outtmpl": os.path.join(
                output_dir,
                "%(title)s.%(ext)s"
            ),
            "merge_output_format": "mp4",
        }

    try:
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])

        print()
        print(f"{GREEN}[!] Téléchargement terminé.")

    except Exception as error:
        print()
        print(f"{RED}[!] Erreur : {error}")


download()