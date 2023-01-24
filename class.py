# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 11:19:28 2022

@author: KIIT
"""

class car:
    name=""
    color=""
    brand=""
    fuel=""
    def __init__(self,name,color,brand,fuel):         
       #__init__ is used for constructor self works as this pointer
       self.name=name
       self.color=color
       self.brand=brand
       self.fuel=fuel
    def __str__(self):
        print(self.name)
        print(self.brand)
        print(self.color)
        print(self.fuel)
        return ""
car1 = car("p1","orange","mclaren","petrol")
print(car1)  
