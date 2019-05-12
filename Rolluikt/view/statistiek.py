'''
Created on 10 mei 2019

@author: daana
'''

LARGE_FONT = ("Verdana", 12)
MEDIUM_FONT = ("Verdana", 12)

from tkinter import *
from tkinter import ttk

from view import main

class statistiekGUI(Frame):

    
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Statistiek", font=LARGE_FONT,background="white")
        label.pack()
        