# Handles reading and writing of all application settings.

CONFIG_FILE = "config.toml" # Application configuration file.

import tomllib
from pathlib import Path

class Config:
    def __init__(self):
        """Initialize the configuration settings.
        """
        self.config = None
        
        try:
            self.config = tomllib.loads(Path(CONFIG_FILE).read_text(encoding="utf-8"))
        except Exception as error:
            print(error, "\nVerify your \"config.toml\" file exists.")
            exit()
        
    def is_config_loaded(self):
        if None in [self.config]:
            return False
        else:
            return True
