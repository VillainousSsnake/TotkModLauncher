# TotkModLauncher/gui/index.py
# Contains Index class for screens

# Importing screens and gui's
from gui.main_menu import main_menu
from gui.settings_menu import settings_menu


# Index class
class Index:
    # Main Menu
    @staticmethod
    def main_menu(self):
        main_menu(self)
    
    # Settings Menu
    @staticmethod
    def settings_menu(self):
        settings_menu(self)

    # Manage Menu
    @staticmethod
    def manage_menu(self):
        pass  # TODO: Stub

    # Download Menu
    @staticmethod
    def download_menu(self):
        pass  # TODO: Stub
