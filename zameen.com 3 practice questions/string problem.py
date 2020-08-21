s="<div><div><b></b></div></p>"
i=0
t1=[]
t2=[]
while(i<len(s)):
    w=''
    if(s[i]=='<'):
        while(s[i]!='>'):
            w=w+s[i]
            i+=1
#        push starting tag in list 1
#        push ending tag in list 2
        if(w[0]=='<')and (w[1]!='/'):
            t1.append(w[1:])
            
        elif(w[0]=='<' and w[1]=='/'):
            t2.append(w[2:])   
    else:
        i+=1
print(t1,t2)
t2=t2[::-1]
f=True
while(len(t1)>0 and len(t2)>0):
    x=t1.pop()
    y=t2.pop()
    if(x!=y):
        break
print(x)    
    



     
#str1=str1.split(">")
#tag1=[]
#tag2=[]
#print(str1)
#for i in str1:
#    l=str(i)
#    print(l)
#    if(len(l)>0):
#        if(l[0]=='<')and (l[1]!='/'):
#            tag1.append(l[1:])
#        elif(l[0]=='<' and l[1]=='/'):
#            tag2.append(l[2:])
#print(tag1,tag2)            
#
#str1="<div><b><p>hello world</p></b></div>"
#for i in range(0,len(str1)):
#    if(str1[i]=='<'):
#        while(1):
#            if(str1[i]=='>'):
#                break
#            else:
#                s+=str1[i]
#    


