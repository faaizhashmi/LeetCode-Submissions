S=input()
T=input()
count=0;
for i in range(0,len(S)):
    if (T[i]!=S[i]):
        count+=1
print(count)