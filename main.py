#Downloads organizer

__author__ = "KeyboardBasher"
__credits__ = ["KeyboardBasher"]
__version__ = "0.0.1"
__maintainer__ = "KeyboardBasher"
__status__ = "Development"
__name__ = "Downloads Organizer"

# Validate the sort folders as defined in the config.toml file.
for sort_folder in SORT_FOLDERS:
    
    sort_folder_path = sort_folder["folder_path"]
    
    # If the sort folder path does not exist, create it.
    if Path(sort_folder_path).exists():
        pass
    else:
        Path.mkdir(sort_folder_path)

exit()
