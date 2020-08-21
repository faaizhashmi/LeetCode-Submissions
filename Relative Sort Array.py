arr1 = [2,1,4,3,9,6]
arr2 = [2,3,1,3,2,4,6,7,9,2,19]
arr3=[]
for i in arr1:
    for j in arr2:
        if(i==j):
            arr3.append(i)

for i in arr2:
    if(arr3.count(i)==0):
        arr3.append(i)

print(arr3)         