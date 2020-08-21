#It has at least 6 characters and at most 20 characters.
#It must contain at least one lowercase letter, at least one uppercase letter, and at least one
# digit.
#It must NOT contain three repeating characters in a row ("...aaa..." is weak, but "...aa...a..."
# is strong, assuming other conditions are met
pas=""
low=False
up=False
dig=False
count=0
n=len(pas)
if (n<6):
    count=count+(6-n)
if (n>20):
    count=count+(n-20)    
for i in pas:
    if(i.isupper()):
        up=True
    if(i.islower()):
        low=True
    if(i.isdigit()):
        dig=True
if (not low):
    count+=1
if (not up):
    count+=1
if (not dig):
    count+=1

for i in range(0,len(pas)-2):
    if(pas[i]==pas[i+1] and pas[i+1]==pas[i+2]):
        count+=1
print(count)      