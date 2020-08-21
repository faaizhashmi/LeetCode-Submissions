n=2147483648
if(n>=abs(2147483647)):
    print("size reached")
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
s=0
t=1
for i in range(len(l)-1,-1,-1):
   s=s+(l[i]*t)
   t=t*10   
if(k<0):
    s=-s
print(s)    