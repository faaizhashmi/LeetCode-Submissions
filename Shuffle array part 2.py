# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 09:08:58 2020

@author: Faaiz Laptop
"""

s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
s=list(s)
l=s.copy()
s1=""
print(s)

for i in range(0,len(indices)):
    l[indices[i]]=s[i]
    
for i in l:
    s1=s1+i 
print(s1)