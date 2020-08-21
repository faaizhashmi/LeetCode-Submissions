n=4421
l=[]
print(n)
while(n>0):
    k=n%10
    l.append(k)
    n=int(n/10)
p=1
s=0
for i in l:
   p=p*i
   s=s+i
print(p-s)     