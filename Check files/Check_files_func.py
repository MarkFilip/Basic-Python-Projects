from tkinter import *
from tkinter import filedialog
import tkinter as tk


# Import other modules
import Check_files_main
import Check_files_gui

def browse1(self):
    sel_directory = filedialog.askdirectory()
    self.txt_browse1.delete(0,END)
    self.txt_browse1.insert(0,sel_directory)

def browse2(self):
    sel_directory = filedialog.askdirectory()
    self.txt_browse2.delete(0,END)
    self.txt_browse2.insert(0,sel_directory)


if __name__ == "__main__":
    pass
