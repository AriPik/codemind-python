arr=list(map(int,input().split()))
b=[]
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        b.append((arr[i]-1)*(arr[j]-1))
print(max(b))        