# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 10:21:33 2022

@author: KIIT


f=open("test.txt","w")
f.write("Bikramaditya Munshi \n")
f.write("Age-18")
f=open("test.txt","r+")
print(f.readlines())
f.close()

def intro():
    print("NAME: Bikramaditya Munshi")
    print("ROLL: 2105538")
    print("AGE:  18")
    
intro()
"""
"""
def sum(x,y=2):
    print(x+y)
sum(420)
"""
"""
def scope():
    x=10
    print(x) #output 10
x=50
scope()
print(x)   #output 50
"""
def pow(x,y):
    if y!=1:
        return(x*pow(x,y-1))
    elif y==1:
        return x
    elif y==0:
        return 1
    
    
print(pow(2,3))