# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 08:15:32 2020

@author: Faaiz Laptop
"""

num = 14
s=0
while(1):
    if(num==0):
        break
    elif num%2==0:
        num=num/2
        s+=1
    else:
        num=num-1
        s+=1
print(s)