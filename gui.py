# Graphical User Interface module.

import customtkinter as ctk

class MainApp(ctk.CTk):
    def __init__(self, program_name):
        super().__init__()
        
        self.title(program_name)
        self.geometry("400x220")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        