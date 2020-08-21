n=9999
print(n)
l=[]
k=n
k1=0
while(n>0):
    k1=n%10
    l.append(k1)
    n=int(n/10)
l=l[::-1]

for i in range(0,len(l)):
    if(l[i]==6):
        l[i]=9
        break
print(l)        
s=0
t=1
for i in range(len(l)-1,-1,-1):
   s=s+(l[i]*t)
   t=t*10  
return s