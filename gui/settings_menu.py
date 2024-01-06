# TotkModLauncher/gui/settings_menu.py
# Contains settings_menu function

# Importing dependencies
from tkinter import filedialog
import tkinter as tk
import ctypes as ct
import os


# Defining settings_menu
def settings_menu(self):

    # Creating root window
    root = tk.Tk()
    root.title("TotkModLauncher")
    root.geometry("500x500+200+200")
    root.configure(bg="#131642")
    root.resizable(False, True)

    # Making the title bar dark mode
    root.update()
    ct.windll.dwmapi.DwmSetWindowAttribute(ct.windll.user32.GetParent(root.winfo_id()), 20, ct.byref(ct.c_int(2)),
                                           ct.sizeof(ct.c_int(2)))

    # Defining on_close function
    def on_close():
        root.destroy()
        self.returnStatement = "QUIT"

    # Assigning the on_close function to the exit button on root
    root.protocol("WM_DELETE_WINDOW", on_close)

    # Button Functions
    def back_button_command():
        root.destroy()
        self.returnStatement = "-MAIN-"

    def choose_romfs_loc_button_command():
        # Setting the app var romfsLocation to the returned directory
        self.romfsLocation = filedialog.askdirectory()

        # read the app lib
        with open(os.path.join(os.getcwd(), "lib", "app.py"), "r") as appFile:
            appFileLines = appFile.readlines()

        # Go through all the lines until it finds 'self.romfsLocation ='
        output = ""
        for line in appFileLines:

            # Detect "self.romfsLocation = "
            if "self.romfsLocation = " in line:
                output += "        self.romfsLocation = " + "'" + str(self.romfsLocation) + "'\n"
            else:
                output += line

        # Writing output to app.py
        with open(os.path.join(os.getcwd(), "lib", "app.py"), "w") as appFile:
            appFile.write(output)

        # Destroying the currentRomfsLabel and creating a new one
        currentRomfsLabel.update()

        # Print log
        print("Set RomFS folder to: '" + str(self.romfsLocation) + "'")

    # Button Definitions
    backButton = tk.Button(root, text="<--", command=back_button_command, bg="#8b41bf",
                           borderwidth=2, highlightcolor="#ba75eb")
    backButton.place(x=0, y=0)

    chooseRomfsLocButton = tk.Button(root, text="Choose", command=choose_romfs_loc_button_command, bg="#8b41bf",
                                     borderwidth=2, highlightcolor="#ba75eb", height=1)
    chooseRomfsLocButton.place(x=395, y=50)

    # Creating Labels
    setRomfsLabel = tk.Label(text="RomFS Location: ", bg="#8b41bf", highlightbackground="#ba75eb", highlightthickness=2,
                             cursor="left_ptr")
    setRomfsLabel.place(x=45, y=50)

    currentRomfsLabel = tk.Label(text=str(self.romfsLocation))
    currentRomfsLabel.place(x=150, y=52.5)

    # mainloop
    root.mainloop()
