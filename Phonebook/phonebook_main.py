# Pyhton Ver:   3.8.2
#
# Author:       Mark Filipkowski
#
# Purpose:      Create a Phonebook demonstrating OOP, Tkinter GUI module,
#               using Tkinter PArent and Child relationships
#
# Tested OS:    THis code was written and tested with Windows 10
#

from tkinter import *
import tkinter as tk

# Importing our other modules for access
import phonebook_gui
import phonebook_func

# Frame is the Tkinter frame class we are inheriting from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define master frame configuration
        self.master = master
        self.master.minsize(500,300)    #(H,W)
        self.master.maxsize(500,300)
        # CenterWindow method will center our app on the user's screen
        phonebook_func.center_window(self,500,300)
        self.master.title("The Tkinter Phonebook Demo")
        self.master.configure(bg="#F0F0F0")
        # This protocol is a tkinter built-in method to catch if
        # the user clicks the upper corner, "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg = self.master

        # load in the GUI widgets from a separate module,
        # keeping your code comparmentalized and clutter free
        phonebook_gui.load_gui(self)

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
