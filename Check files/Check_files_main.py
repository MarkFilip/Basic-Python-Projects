from tkinter import *
from tkinter import filedialog
import tkinter as tk

# Import other modules
import Check_files_gui
import Check_files_func



class ParentWindow(Frame):
    def __init__(self,master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #define master frame configuration
        self.master = master
        #self.master.minsize(740,280)
        #self.master.maxsize(740,280)
        self.master.title("Check Files")
        self.master.configure(bg="#F0F0F0")

        # load in GUI widegets from other module
        Check_files_gui.load_gui(self)
        

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()


        
        
        
