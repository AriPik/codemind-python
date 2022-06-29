n=int(input())
arr=list(map(int,input().strip().split()))
b=[]
k=0
for i in range(n):
    if(arr.count(arr[i])==1):
        b.append(arr[i])
        k=1
if (k==0):
    print("-1")
else:
    print(max(b))