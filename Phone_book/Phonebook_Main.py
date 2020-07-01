#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Python Version: 3.7.5
#
# Author: Steven J. Carney
#
# Purpose: To demonstrate how OOP, Tkinter GUI, and SQL can work together
#
# Tested OS: This code is known to work on WIndows 10
#

from tkinter import *
import tkinter as tk
from tkinter import messagebox

# Import other related modules

import Phonebook_Gui
import Phonebook_Func

# Frame is the Tkinter frame class that our own class will inherit from

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)


        # Define our master frame configuration
        self.master = master
        self.master.minsize(500,300) # (Height, Width)
        self.master.maxsize(500,300)
        # This CenterWindow method will center our app on the user's screen
        Phonebook_Func.center_window(self,500,300)
        self.master.title("The Tkinter Phonebook Demo")
        self.master.configure(bg="#F0F0F0")
        # This protocol method is a tkinter built-in method to catch if
        # the user clicks the upper corner, "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: Phonebook_Func.ask_quit(self))
        arg = self.master

        # load in the GUI widgets from a separate modules,
        # keeping the code compatmentalized and clutter free
        Phonebook_Gui.load_gui(self)
                
        # Instantiate the Tkinter menu dropdown object
        # This is the menu that will appear at the top of our window
        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", underline=1,accelerator="Ctrl+Q",command=lambda: Phonebook_Func.ask_quit(self))
        menubar.add_cascade(label="File", underline=0, menu=filemenu)
        helpmenu = Menu(menubar, tearoff=0) # defines the particular drop down colum and tearoff=0 means do not separate from menubar
        helpmenu.add_separator()
        helpmenu.add_command(label="How to use this program")
        helpmenu.add_separator()
        helpmenu.add_command(label="About This Phonebook Demo") # add_command is a child menubar item of the add_cascde parent item
        menubar.add_cascade(label="Help", menu=helpmenu) # add_cascade is a parent menubar item (visible heading)
        self.master.config(menu=menubar, borderwidth='1')

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()