#!/usr/bin/python
# -*- coding: utf-8 -*-

import shutil
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import os
import time





class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        # Define our master frame configuration
        self.master = master
        self.text = tk.StringVar()
        self.master.minsize(700,300) # (Height, Width)
        #self.master.maxsize(1000,600)
        self.master.resizable(True, True)
        # This CenterWindow method will center our app on the user's screen
        center_window(self,700,300)
        self.master.title("Daily File Sort")
        self.master.configure(bg="darkgrey")
        # This protocol method is a tkinter built-in method to catch if
        # the user 
        # clicks the upper corner, "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: ask_quit(self))
        arg = self.master
        load_GUI(self)

#Functions for setting up the user interface
def load_GUI(self):


    self.btn_sort = tk.Button(self.master, width=10, height=1, text="Sort", command=lambda: onSort(self))
    self.btn_sort.grid(row=1, column=1, padx=(15,15), pady=(15, 15), sticky=W)
    self.btn_quit = tk.Button(self.master, width=10, height=1, text="Quit", command=lambda: ask_quit(self))
    self.btn_quit.grid(row=2, column=1, columnspan=2, padx=(15,15), pady=(10, 10), sticky=W)
        
    self.lbl_dst = tk.Label(self.master, text="Destination Folder") 
    self.lbl_dst.grid(row=1, column=2, columnspan = 2, padx=(15, 15), pady=(10,10), sticky=W)
#    self.btn_dst = tk.Button(self.master, width=10, height=1, text="Destination", command=lambda: onDestination(self, dstFolder))
#    self.btn_dst.grid(row=4, column=1, columnspan=2, padx=(15,15), pady=(10, 10), sticky=W)

    
    self.lbl_src = tk.Label(self.master, text="Source Folder") 
    self.lbl_src.grid(row=2, column=2, columnspan = 2, padx=(15, 15), pady=(10,10), sticky=W)
#    self.btn_src = tk.Button(self.master, width=10, height=1, text="Source", command=lambda: onSource(self, dstFolder))
#    self.btn_src.grid(row=3, column=1, columnspan=2, padx=(15,15), pady=(10, 10), sticky=W)

def center_window(self, w, h): # pass in the tkinter frame (Master) reference and the w and h
    # get users screen width and heith
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo

# catch if the user clicks on the 'X" to ensure they want to close
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Quit?"):
        #This closes the app
        self.master.destroy()
        os._exit(0)

#Functions for choosing, Source Dir, and Destination Dir
   
def onSort(self):
    try:

        #Creates a browser to select the source folder
        srcFolder = filedialog.askdirectory()
        self.lbl_src.config(text=srcFolder)
        print(srcFolder)
        time.sleep(.5)

        #Creates a browser to select the destination folder
        dstFolder = filedialog.askdirectory()
        self.lbl_dst.config(text=dstFolder)
        print(dstFolder)
        time.sleep(.5)


        #Sort function, sorting todays tickets
        SECONDS_IN_DAY = 24 * 60 * 60
        now = time.time()
        before = now - SECONDS_IN_DAY


        if messagebox.askokcancel("Sort Files", "Files will be moved to Destination Folder, \nWould you like to continue?"):

            def last_mod_time(fname):
                return os.path.getmtime(fname)

            for fname in os.listdir(srcFolder):
                src_fname = srcFolder + "/" + fname
                if last_mod_time(src_fname) > before:
                    dst_fname = dstFolder + "/" + fname
                    shutil.move(src_fname, dst_fname)
                    if messagebox.askokcancel("Alert", "File move complete!"):
                        ask_quit(self)
                else:
                    ask_quit(self)
            print("Done!")
        else:
            ask_quit(self)


    except Exception as e: 
        messagebox.askokcancel("Error", e)
        print(e)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

