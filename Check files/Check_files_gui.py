from tkinter import *
from tkinter import filedialog
import tkinter as tk

# Import other modules
import Check_files_main
import Check_files_func

def load_gui(self):
    # Text boxes
    self.txt_browse1 = tk.Entry(self.master,text='')
    self.txt_browse1.grid(row=0, column=1, rowspan=1, columnspan=3, padx=(0,20),pady=(40,0), sticky=N+E+W)
    self.txt_browse2 = tk.Entry(self.master,text='')
    self.txt_browse2.grid(row=1, column=1, rowspan=1, columnspan=3, padx=(0,20),pady=(10,0), sticky=N+E+W)

    # Buttons
    self.btn_browse1 = tk.Button(self.master, width=12, height=1, text='Browse...',command=lambda: Check_files_func.browse1(self))
    self.btn_browse1.grid(row=0, column=0,padx=(20,25),pady=(40,0))
    self.btn_browse2 = tk.Button(self.master, width=12, height=1, text='Browse...',command=lambda: Check_files_func.browse2(self))
    self.btn_browse2.grid(row=1, column=0,padx=(20,25),pady=(10,0))
    self.btn_check = tk.Button(self.master,width=12, height=2, text='Check for files...')
    self.btn_check.grid(row=2, column=0, rowspan=2, padx=(20,25),pady=(10,20))
    self.btn_close = tk.Button(self.master,width=12, height=2, text='Close Program')
    self.btn_close.grid(row=2, column=3, rowspan=2, padx=(180,20),pady=(10,20))
    

    


if __name__ == "__main__":
    pass
