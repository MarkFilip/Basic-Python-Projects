from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk
import os
import sqlite3
import time
import shutil


# Import other modules
import Check_files_main
import Check_files_gui


# Asks the user to pick a file in their directory and
# displays the results in the corresponding text box
def browse1(self):
    sel_directory = filedialog.askdirectory()
    self.txt_browse1.delete(0,END)
    self.txt_browse1.insert(0,sel_directory)

def browse2(self):
    sel_directory = filedialog.askdirectory()
    self.txt_browse2.delete(0,END)
    self.txt_browse2.insert(0,sel_directory)

def full_path(dir_path,file_name):
    """
        Joins the directory and the file name
        to get the absolute file path.
    """
    full_path = os.path.join(dir_path,file_name)
    return full_path

def create_db():
    """
        Creates a database with and empty table
        where .txt files that will be moved are
        stored alongside their last modified date.
    """
    conn = conn = sqlite3.connect('file_moved.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_files ( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            file_name TEXT, \
            date_modified TEXT \
            )")
        conn.commit()
    conn.close

def fill_db(affected_files,date_mod):
    """
        Fills the database with the names and last
        modified dates of files to be moved to the
        new directory.
    """
    conn = sqlite3.connect('file_moved.db')
    with conn:
        cur = conn.cursor()
        for i in range(len(affected_files)):    
            cur.execute("INSERT INTO tbl_files(file_name,date_modified) VALUES (?,?)", \
                            (affected_files[i],date_mod[i])) 
        conn.commit()
    conn.close
    
def check(self):
    """
        Finds text files in a source directory and moves
        them into the destination directory while creating
        a database with the files moved and prints the file
        names and date last modified to the console.
    """
    source_dir = self.txt_browse1.get()
    dest_dir = self.txt_browse2.get()
    affected_files = []
    date_mod = []
    # First it has to check if there are directory paths
    # chosen in the text box. If not it will display an error.
    if source_dir =="" or dest_dir == "":
        messagebox.showerror("Error","A directory path has not been chosen")
    else:   # Creates a list of the .txt files
        file_list=os.listdir(source_dir)
        for i in file_list:
            if i.endswith('.txt') == True:
                affected_files.append(i)
    for i in affected_files:    # Creates a list of the date last modified for each .txt file
        mtime = os.path.getmtime(full_path(source_dir,i))
        time_obj = time.localtime(mtime)
        if time_obj[3] > 12:
            date_modified = ("{}/{}/{} {}:{} PM".format(time_obj[1],time_obj[2],time_obj[0],(time_obj[3]-12),time_obj[4]))
        elif time_obj[3] == 12:
            date_modified = ("{}/{}/{} 12:{} PM".format(time_obj[1],time_obj[2],time_obj[0],time_obj[4]))
        elif time_obj[3] == 0:
            date_modified = ("{}/{}/{} 12:{} AM".format(time_obj[1],time_obj[2],time_obj[0],time_obj[4]))
        else:
            date_modified = ("{}/{}/{} {}:{} AM".format(time_obj[1],time_obj[2],time_obj[0],time_obj[3],time_obj[4]))
        date_mod.append(date_modified)                               
    create_db()
    fill_db(affected_files,date_mod)
    for i in range(len(affected_files)):
        print("\nFile name:\n")
        print(affected_files[i])
        print("\nDate last modified (MM/DD/YYYY):\n")
        print(date_mod[i])
    for i in affected_files:
        shutil.move(full_path(source_dir,i),dest_dir)

def close(self):
    if tk.messagebox.askokcancel("Close program", "Okay to close the application?"):
        # This closes the app
        self.master.destroy()
        os._exit(0)
        

if __name__ == "__main__":
    pass
