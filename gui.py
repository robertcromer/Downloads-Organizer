# Graphical User Interface module.

import customtkinter as ctk
import organizer

class MainApp(ctk.CTk):
    def __init__(self, program_name: str, config):
        super().__init__()
        
        self.organizer = organizer.Organizer(config.config)
        
        self.title(program_name)
        self.geometry("400x220")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        self.organize_button = ctk.CTkButton(
                        master=self,
                        text="Organize Downloads",
                        command=self.organize_callback
        )
        self.organize_button.grid(
                        row=0,
                        column=0,
                        padx=20,
                        pady=20
        )
        
        self.organized_files_label = ctk.CTkLabel(
                        master=self,
                        text="0 files moved."
        )
        self.organized_files_label.grid(
                        row=1,
                        column=0,
                        padx=5,
                        pady=5
        )
    
    def organize_callback(self):
        self.organizer.validate_sort_folders()
        self.organizer.get_downloaded_files()
        self.organizer.organize()
        self.organized_files_label.configure(text=f"{self.organizer.qty_files_moved} files moved.")
