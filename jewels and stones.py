# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 07:47:12 2020

@author: Faaiz Laptop
"""
J = "aA"
S = "aAAbbbb"
count=0
for i in J:
    k=S.count(i)
    count=count+k
print(count)    