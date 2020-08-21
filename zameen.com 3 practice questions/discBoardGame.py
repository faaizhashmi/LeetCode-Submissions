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
    

b=["(x,x,x,x,x,x,x)","(x,x,x,x,x,x,x)","(x,x,x,R,x,x,x)","(x,x,x,R,x,x,x)","(x,x,x,R,x,x,x)","(x,x,x,R,Y,Y,Y)"]    

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

for i in b:
    print(i)

l1=[]
i=2
j=3
while(i<(i+4) and i<6):
    l1.append(l[i][j])
    i+=1
match=True
try:
    l1.remove('x')
except:
    pass    
for i in range(0,len(l1)-1):
    if(l1[i]!=l1[i+1] or len(l1)!=4 ):
        match=False
        break
if(match):
    print("check!")          



l1=[]
i=2
j=3
while(i>(i-4) and i>=0):
    l1.append(l[i][j])
    i-=1
match=True
try:
    l1.remove('x')
except:
    pass 
for i in range(0,len(l1)-1):
    if(l1[i]!=l1[i+1]  or len(l1)!=4 ):
        match=False
        break
if(match):
    print("check!")          



l1=[]
i=2
j=3
while(j>(j-4) and j>=0):
    l1.append(l[i][j])
    j-=1    
match=True
try:
    l1.remove('x')
except:
    pass 
for i in range(0,len(l1)-1):
    if(l1[i]!=l1[i+1]  or len(l1)!=4 ):
        match=False
        break
if(match):
    print("check!")          
   



l1=[]
i=2
j=3
while(j<(j+4) and j<7):
    l1.append(l[i][j])
    j+=1
match=True
try:
    l1.remove('x')
except:
    pass 
for i in range(0,len(l1)-1):
    if(l1[i]!=l1[i+1]  or len(l1)!=4 ):
        match=False
        break
if(match):
    print("check!")          
   



l1=[]
i=2
j=3
while((i<(i+4) and i<6) and (j<(j+4) and j<7) ):
    l1.append(l[i][j])
    i+=1
    j+=1
match=True
try:
    l1.remove('x')
except:
    pass 
for i in range(0,len(l1)-1):
    if(l1[i]!=l1[i+1]  or len(l1)!=4 ):
        match=False
        break
if(match):
    print("check!")          
  



l1=[]    
i=2
j=3   
while((i>(i-4) and i>=0) and (j>(j-4) and j>=0)):
    l1.append(l[i][j])
    i-=1
    j-=1
match=True
try:
    l1.remove('x')
except:
    pass 
for i in range(0,len(l1)-1):
    if(l1[i]!=l1[i+1] or len(l1)!=4 ):
        match=False
        break
if(match):
    print("check!")          
 



l1=[]
i=2
j=3
while((i<(i+4) and i<6) and ((j>(j-4) and j>=0))):
    l1.append(l[i][j])
    i+=1
    j-=1   
match=True
try:
    l1.remove('x')
except:
    pass 
for i in range(0,len(l1)-1):
    if(l1[i]!=l1[i+1] or len(l1)!=4 ):
        match=False
        break
if(match):
    print("check!")          




l1=[]
i=2
j=3
while((j<(j+4) and j<7) and(i>(i-4) and i>=0)):
    l1.append(l[i][j])
    i-=1
    j+=1
    
match=True
try:
    l1.remove('x')
except:
    pass 
for i in range(0,len(l1)-1):
    if(l1[i]!=l1[i+1] or len(l1)!=4 ):
        match=False
        break
if(match):
    print("check!")

#checking upper layer

#l=[]
#for i in range(0,len(b)):
#    l1=[]
#    for j in range(0,len(b[0])):
#        if(b[i][j]=='x' or b[i][j]=='R' or b[i][j]=='Y'):
#            l1.append(b[i][j])
#    if(len(l1)>0):
#        l.append(l1)    

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
