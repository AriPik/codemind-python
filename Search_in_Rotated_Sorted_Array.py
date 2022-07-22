n=int(input())
l=list(map(int,input().split()))[:n]
k=int(input())
ind=0
for i in l:
    ind=0
    if i==k:
        ind=l.index(k)
        break
if ind:
    print(ind)
else:
    print("-1")