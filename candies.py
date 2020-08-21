# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 05:42:56 2020

@author: Faaiz Laptop
"""
import numpy 
candies = [12,1,12]
extraCandies = 10
n=extraCandies
max_value = numpy.max(candies)
arr1=[]
print(max_value)
for i in candies:
    if n+i >=max_value:
        arr1.append(True)
    else:   
        arr1.append(False)
print(arr1)        