# TotkModLauncher/tml/main.py
# Contains main program

# Importing Modules and Packages
from lib.app import App
from gui.index import Index

# Creating App
app = App()

# Main loop
while app.returnStatement != "QUIT":
    # Checking returnStatement and running
    #  the corresponding screen
    if app.returnStatement == "-MAIN-":
        Index.main_menu(app)
    if app.returnStatement == "LAUNCH-MODS":
        pass  # TODO: Stub
    if app.returnStatement == "MANAGE":
        pass  # TODO: Stub
    if app.returnStatement == "SETTINGS":
        Index.settings_menu(app)
    if app.returnStatement == "DOWNLOAD":
        pass  # TODO: Stub
