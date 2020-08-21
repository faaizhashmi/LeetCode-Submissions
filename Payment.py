# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 11:16:21 2020

@author: Faaiz Laptop
"""

N=int(input())
if(N%1000==0):
    print(0)
else:
    print(1000-(N%1000))    