# Organizer of all downloaded files.

from pathlib import Path, PurePath
from shutil import move

class Organizer:
    def __init__(self, config_settings):
        self.config_settings = config_settings
        self.downloads = []
        self.downloads_folder = Path(self.config_settings["downloads"]["folder_path"])
        self.sort_folders = self.config_settings["folders"]
    
    def validate_sort_folders(self):
        for sort_folder in self.sort_folders:
            """Something is producing an error in this method.
                It cannot find the path specified.
            """
            sort_folder_path = sort_folder["folder_path"]
            
            # If the sort folder path does not exist, create it.
            if Path(sort_folder_path).exists():
                pass
            else:
                Path.mkdir(sort_folder_path)
    
    def get_downloaded_files(self):
        for file in Path.iterdir(self.downloads_folder):
            if Path.is_file(file):
                self.downloads.append(file)
            else:
                pass
    
    def organize(self):
        # Iterate through all of the files in the downloads list.
        self.qty_files_moved = 0
        for unsorted_file in self.downloads:
            for sort_folder in self.sort_folders:
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
                        self.qty_files_moved += 1
                    except OSError as error:
                        print (error)
                else:
                    pass
        print(f"{self.qty_files_moved} files moved.")


