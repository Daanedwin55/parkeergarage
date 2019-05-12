'''
Created on 10 mei 2019

@author: daana
'''
from model import grid

class car():
    def __init__(self, hastopay, minutesleft):
        self.hastopay =hastopay
        self.minutesleft =minutesleft
    
    def setColor(self, color):
        self.color = color
            
    def getColor(self):
        return self.color
    
    def getHasToPay(self):
        return self.hastopay
    
    def getMinutesLeft(self):
        return self.minutesleft
            
    def tick(self):
        self.minutesleft = (self.minutesleft - 1)

class normalcar(car):
    def __init__(self, color, minutesleft):
        hastopay = True
        super().__init__(hastopay,minutesleft)
        
        super().setColor(color)

           
class passcar(car):
    def __init__(self, color, minutesleft):
        hastopay = False
        super().__init__(hastopay,minutesleft)
        
        super().setColor(color)
        
        
        
        
        
    
        
    
