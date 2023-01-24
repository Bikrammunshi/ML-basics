# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 12:12:55 2022

@author: KIIT
"""

import numpy as np
"""
d=np.array([[1,2],[3,4]])
print(d)
data=np.array([1,2,3,4])
print(data)
dat=np.arange(0,10,1)
print(dat)
print(np.zeros((2,3,4)))
print(np.ones(10))
"""



#print(np.arange(2000,15,-3))

#print(np.linspace(10,20))
#print(np.linspace(0,1,20))
#print(np.eye(5))
#print(np.random.rand(5,2))
#print(np.random.randint(0,10,(2,5)))
#first argument is start second argument is end and third argument 
# is the size of the matrix
#print(np.random.rand(5,5))
#print(np.random.randn(10))#random numbers close to zero



"""

arr=np.random.randn(10)
print(arr)
print(arr.shape)#shape is an attribute
arr2=arr.reshape(2,5)
print(arr2)
print(arr.max())
print(arr.argmax())

"""
"""
arr=np.random.randint(0,10,(5,5))
print(arr)
print(arr[1:4,1:4])
arr[1:4,1:4]=10
print(arr)
arr2=np.random.randint(0,10,(5,5))
print(arr2)
print(arr+arr2)
"""
"""
arr=np.zeros(10)
arr2=np.ones(10)
print(arr2/arr)
"""

arr1=np.random.randint(0,10,10)
arr1=arr1+10
print(arr1)
print(np.sqrt(arr1))
print(np.sin(arr1))