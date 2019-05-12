'''
Created on 10 mei 2019

@author: daana
'''

from tkinter import *

from view import main, instellingen, statistiek

import threading

class root(Tk):
    def __init__(self, *args, **kwargs):
        
        Tk.__init__(self, *args, **kwargs)
        
        Tk.title(self, "Parkeergarage Python")
        Tk.maxsize(self, 1200, 800)
        Tk.minsize(self, 800, 500)
        Tk.config(self, background="white")
        
        scherm = Frame(self)
        scherm.grid(row=0, column=2, sticky="nsew")
        scherm.grid_rowconfigure(0, weight=1)
        scherm.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
                
        for F in (main.mainGUI, instellingen.instellingGUI, statistiek.statistiekGUI):
            
            frame = F(scherm, self)
            
            self.frames[F] = frame
            
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show(main.mainGUI)

        self.update()
    def show(self, scherm):           
        frame = self.frames[scherm]
        frame.tkraise()
    
        
    
        
app = root()
app.mainloop()

