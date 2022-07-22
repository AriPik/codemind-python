n=int(input())
l=list(map(int,input().split()))[:n]
l1=[]
k=n//2
for i in range(n-1,k-1,-1):
    l1.append(l[i])
for i in range(0,k):
    l1.append(l[i])
print(*l1)