# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 08:33:16 2020

@author: Faaiz Laptop
"""

the_string = input()
L1,R1,d1 = the_string.split()
L=int(L1)
R=int(R1)
d=int(d1)
count=0
for i in range(L,R+1):
    if(i%d)==0:
        count+=1
print(count)        