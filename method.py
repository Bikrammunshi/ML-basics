# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 11:48:52 2022

@author: KIIT
"""

class point:
    x=0
    y=0
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return ("("+str(self.x)+"."+str(self.y)+")")
    def distance(self):
        return((self.x**2+self.y**2)**0.5)
    
a=point(3,4)
print(a)
print(a.distance())