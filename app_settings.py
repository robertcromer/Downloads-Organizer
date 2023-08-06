# Handles reading and writing of all application settings.

CONFIG_FILE = "config.toml" # Application configuration file.

import tomllib
from pathlib import Path, PurePath

config = None
downloads = []
downloads_folder = None
sort_folders = None

def is_config_loaded():
    if config != None:
        return True
    else:
        return False

def load_config():
    config = tomllib.loads(Path(CONFIG_FILE).read_text(encoding="utf-8"))

def get_downloads_folder():
    downloads_folder = Path(config["downloads"]["folder_path"])

def get_sort_folders():
    sort_folders = config["folders"]


