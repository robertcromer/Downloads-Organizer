# Organizer of all downloaded files.

from pathlib import Path, PurePath
from shutil import move

def get_downloaded_files():
    for file in Path.iterdir(downloads_folder):
        if Path.is_file(file):
            downloads.append(file)
        else:
            pass