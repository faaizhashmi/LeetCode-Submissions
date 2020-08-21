n=9669
#n=669
#n=9996
#n=9999
print(n)
k=n
k1=0
if(n<0):
    n=-n
l=[]
while(n>0):
    k1=n%10
    l.append(k1)
    n=int(n/10)
print(l)
i=len(l)-1
while(1):
    if(l[i]==6 or i==0):
        l[i]=9
        break
    
    i-=1    
        
s=0
t=1
for i in range(len(l)-1,-1,-1):
   s=s+(l[i]*t)
   t=t*10  
print(s)