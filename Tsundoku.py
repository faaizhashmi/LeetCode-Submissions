# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 20:48:35 2020

@author: Faaiz Laptop
"""
K=730
A=[60, 90, 120]
B=[80, 150, 80, 150]
lastA=A.pop()
lastB=B.pop()
count=0
while(1):
    if(K<lastA and K<lastB):
        break
    print(A,lastA,K)
    print(B,lastB,K)
    if(lastA>lastB):
        K=K-lastB
        lastB=B.pop()
    else:
        K=K-lastA
        lastA=A.pop()
    count+=1    
print(count)