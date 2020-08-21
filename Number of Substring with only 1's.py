# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 23:42:07 2020

@author: Faaiz Laptop
"""

s = "101101001110"
u={}
i=0;
while(i<len(s)):
    cons=0
    sub=''
    while s[i]=='1':
        cons+=1
        sub=sub+'1'
        try:
            u[sub]=u[sub]+1
        except:
            u[sub]=1
        i+=1  
    i+=1
print(u)        