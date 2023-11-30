# TotkModLauncher/bin/main.py
# Contains main program

# Importing Modules and Packages
from lib.app import App

# Creating App
app = App()

# Main loop
while app.returnStatement != "QUIT":
    # Checking returnStatement and running
    #  the corresponding screen
    if app.returnStatement == "-MAIN-":
        pass  # TODO: Stub
    if app.returnStatement == "LAUNCH-MODS":
        pass  # TODO: Stub
    if app.returnStatement == "MANAGE":
        pass  # TODO: Stub
    if app.returnStatement == "SETTINGS":
        pass  # TODO: Stub
    if app.returnStatement == "DOWNLOAD":
        pass  # TODO: Stub
