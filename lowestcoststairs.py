# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 23:49:33 2020

@author: Faaiz Laptop
"""

cost = [10, 15, 20]
total=0
i=0
while(1):
    if i+1==len(cost) and i+2==len(cost):
        break
    
    elif(cost[i]>cost[i+1]):
        total=total+cost[i+1]
        i+=2
    else:
        total=total+cost[i]
        i+=1
        
print(total)            