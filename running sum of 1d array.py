# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 23:12:47 2020

@author: Faaiz Laptop
"""
nums = [1,2,3,4]
sums=[]
for i in range(0,len(nums)):
    sum1=0;
    for j in range(0,i+1):
        sum1=sum1+nums[j]
    sums.append(sum1)        
print(sums)    