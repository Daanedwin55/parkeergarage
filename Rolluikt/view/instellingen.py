'''
Created on 10 mei 2019

@author: daana
'''

LARGE_FONT = ("Verdana", 12)

from tkinter import *
from tkinter import ttk

from view import main

class instellingGUI(Frame):
    
    def __init__(self, parent, controller):
        
        
        Frame.__init__(self, parent)
        Frame.config(self, background="white")
        label = Label(self, text="Instellingen", font=LARGE_FONT, background="white")
        label.grid(row=0, column=1,pady=15)
        
       