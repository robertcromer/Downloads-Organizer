# Main application.

__author__ = "KeyboardBasher"
__credits__ = ["KeyboardBasher"]
__version__ = "0.0.1"
__maintainer__ = "KeyboardBasher"
__status__ = "Development"
__name__ = "Downloads Organizer"

import app_settings, organizer, gui

config = app_settings.Config()

program_gui = gui.MainApp(program_name=__name__)
program_gui.mainloop()

exit()
