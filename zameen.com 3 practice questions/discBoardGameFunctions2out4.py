# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 02:46:17 2020

@author: Faaiz Laptop
"""

#    initialize a board with disks and spaces
#    function for checking the upper most layer where the disks are to fall
#    function for checking 4 consecutive same colored disks
#    implement control for 2 player taking turns
def givepositions(b):
    l=[]
    for i in range(0,len(b)):
        l1=[]
        for j in range(0,len(b[0])):
            if(b[i][j]=='x' or b[i][j]=='R' or b[i][j]=='Y'):
                l1.append(b[i][j])
        if(len(l1)>0):
            l.append(l1)    
    return l
    
def giveUpperLayer(b):
    c=[]
    l=givepositions(b)    
    i=len(l[0])-1
    while(i>=0):
        j=len(l)-1
        l1=[]
        while(j>=0):
            if(l[j][i]=='x'):
                l1.append(j)
                l1.append(i)
                break
            j-=1
        c.append(l1)    
        i-=1
    c=c[::-1]
    return c

b=["(x,x,x,x,x,x,x)","(x,x,x,x,x,x,x)","(x,x,x,x,x,x,x)","(x,x,x,R,x,x,x)","(x,x,x,R,x,x,x)","(x,x,x,R,Y,Y,Y)"]    

print(giveUpperLayer(b))




##checking upper layer

#l=[]
#for i in range(0,len(b)):
#    l1=[]
#    for j in range(0,len(b[0])):
#        if(b[i][j]=='x' or b[i][j]=='R' or b[i][j]=='Y'):
#            l1.append(b[i][j])
#    if(len(l1)>0):
#        l.append(l1)    
#
#i=len(l[0])-1
#c=[]
#while(i>=0):
#    j=len(l)-1
#    l1=[]
#    while(j>=0):
#        if(l[j][i]=='x'):
#            l1.append(j)
#            l1.append(i)
#            break
#        j-=1
#    c.append(l1)    
#    i-=1
#c=c[::-1]
