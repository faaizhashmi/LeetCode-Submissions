# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 18:39:24 2020

@author: Faaiz Laptop
"""

num=int(input())
i=0
string=""
div=27
while(1):
    print(num)
    num=int(num/div)
    div=div*27
    string=string+"a"
    if(num<=0):
        break
print(string)    
