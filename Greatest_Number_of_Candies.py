n=int(input())
arr=list(map(int,input().strip().split()))
k=int(input())
l=max(arr)
for i in range(n):
    if(arr[i]+k>=l):
        print(True,end=" ")
    else:
        print(False,end=" ")