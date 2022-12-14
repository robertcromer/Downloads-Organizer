#Downloads organizer

__author__ = "KeyboardBasher"
__credits__ = ["KeyboardBasher"]
__version__ = "0.0.1"
__maintainer__ = "KeyboardBasher"
__status__ = "Development"
__name__ = "Downloads Organizer"

CONFIG_FILE = "config.toml" # Program configuration file.

import tomllib
from pathlib import Path, PurePath
from shutil import move

# Load the program configuration file.
config = tomllib.loads(Path(CONFIG_FILE).read_text(encoding="utf-8"))

# Defined constants
# DOWNLOADS_FOLDER is the path to the downloads folder.
DOWNLOADS_FOLDER = Path(config["downloads"]["folder_path"])
# SORT_FOLDERS is a list of all the user defined sorting folders.
SORT_FOLDERS = config["folders"]

# Validate the sort folders as defined in the config.toml file.
for sort_folder in SORT_FOLDERS:
    
    sort_folder_path = sort_folder["folder_path"]
    
    # If the sort folder path does not exist, create it.
    if Path(sort_folder_path).exists():
        pass
    else:
        Path.mkdir(sort_folder_path)

# The downloads list will hold all of the path objects of the downloaded files.
downloads = []

# Iterate through all items inside the downloads folder.
for file in Path.iterdir(DOWNLOADS_FOLDER):
    
    # If the item is a file, add it to the downloads list.
    if Path.is_file(file):
        downloads.append(file)
    else:
        pass

# Iterate through all of the files in the downloads list.
for unsorted_file in downloads:
    for sort_folder in SORT_FOLDERS:
        """Move files to the appropriate folder.
        
        If the extention of the unsorted file in the downloads folder is in
        the listed extensions of the sort folder, move that file to the
        folder as configured in the config.toml file.
        """
        file_suffix = PurePath(unsorted_file).suffix
        extentions = sort_folder["extentions"]
        destination = sort_folder["folder_path"]
        
        if file_suffix in extentions:
            try:
                move(unsorted_file, destination)
            except OSError as error:
                print (error)
        else:
            pass

exit()
