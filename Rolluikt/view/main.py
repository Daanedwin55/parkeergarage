'''
Created on 10 mei 2019

@author: daana
'''

LARGE_FONT = ("Verdana", 12)
MED_FONT = ("Verdana", 10)

import tkinter as tk
from tkinter import *
from tkinter import ttk

from view import instellingen

from view import statistiek

from model import grid
class mainGUI(Frame):

    def __init__(self, parent, controller):

        Frame.__init__(self, parent)
        Frame.config(self, background="white")
        label = Label(self, text="Parkeergarage", font=LARGE_FONT, background="white")
        label.grid(column=0,row=0)
        
        floor1 = Label(self, text=" ", font=MED_FONT, background = "white")
        floor1.grid(column=5,row=2)
        
        tk.Label(text=" ", background = "White",width=8, height=1).grid(row=10,column=5)
        tk.Label(text=" ", background = "White",width=8, height=1).grid(row=10,column=8)
        r = 1
       
        for items in grid.dict1:
            tk.Label(bg=grid.dict1[items], relief=tk.RIDGE,width=8, height=1).grid(row=r,column=3)
            r = r + 1
        r = 1
        
        for items in grid.dict2:
            tk.Label(bg=grid.dict2[items], relief=tk.RIDGE,width=8, height=1).grid(row=r,column=4,padx=2)
            r = r + 1
        r = 1
            
        for items in grid.dict3:
            tk.Label(bg=grid.dict3[items], relief=tk.RIDGE,width=8, height=1).grid(row=r,column=6)
            r = r + 1
        r = 1
            
        for items in grid.dict4:
            tk.Label(bg=grid.dict4[items], relief=tk.RIDGE,width=8, height=1).grid(row=r,column=7,padx=2)
            r = r + 1
        r = 1
           
        for items in grid.dict5:
            tk.Label(bg=grid.dict5[items], relief=tk.RIDGE,width=8, height=1).grid(row=r,column=9)
            r = r + 1
        r = 1
            
        for items in grid.dict6:
            tk.Label(bg=grid.dict6[items], relief=tk.RIDGE,width=8, height=1).grid(row=r,column=10,padx=2)
            r = r + 1    
            
            
        