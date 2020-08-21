ad = "1.1.1.1"
i=0
while(1):
    
    if i >=len(ad):
        break
    if ad[i]=='.':
        ad=ad[:i] + '[' + ad[i]+']'+ad[i+1:]
        i+=1
    i+=1
print(ad)