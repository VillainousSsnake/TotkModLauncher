# TotkModLauncher/gui/main_menu.py
# Contains main_menu function

# Importing dependencies
import tkinter as tk
import ctypes as ct
import os


# Defining main_menu
def main_menu(self):

    # Creating the root window
    root = tk.Tk()
    root.title("TotkModLauncher - Main Menu")
    root.geometry("500x500+200+200")
    root.configure(bg="#131642")
    root.resizable(False, True)

    # Making the title bar dark mode
    root.update()
    ct.windll.dwmapi.DwmSetWindowAttribute(ct.windll.user32.GetParent(root.winfo_id()), 20, ct.byref(ct.c_int(2)), ct.sizeof(ct.c_int(2)))

    # Defining on_close function
    def on_close():
        root.destroy()
        self.returnStatement = "QUIT"

    # Assigning the on_close function to the exit button on root
    root.protocol("WM_DELETE_WINDOW", on_close)

    # Button Functions
    # Defining launch_button_command function
    def launch_button_command():
        pass  # TODO: Stub

    # Defining manage_button_command function
    def manage_button_command():
        root.destroy()
        self.returnStatement = "MANAGE"

    # Defining settings_button_command function
    def settings_button_command():
        root.destroy()
        self.returnStatement = "MANAGE"

    # Creating, initializing, and displaying Buttons
    # Setting up the launchButton
    launchButton = tk.Button(root,
                             text="Launch",
                             command=launch_button_command,
                             width=69,
                             bg="#8b41bf", borderwidth=2,
                             highlightcolor="#ba75eb")
    launchButton.pack(side="top")

    # Setting up manageButton
    manageButton = tk.Button(root,
                             text="Manage Mods",
                             command=manage_button_command,
                             width=69,
                             bg="#8b41bf", borderwidth=2,
                             highlightcolor="#ba75eb")
    manageButton.pack(side="top")

    # Setting up settingsButton
    settingsButton = tk.Button(root,
                               text="Settings",
                               command=settings_button_command,
                               width=69,
                               bg="#8b41bf", borderwidth=2,
                               highlightcolor="#ba75eb")
    settingsButton.pack(side="top")

    # mainloop
    root.mainloop()
