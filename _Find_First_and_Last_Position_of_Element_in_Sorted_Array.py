n=int(input())
l=list(map(int,input().split()))[:n]
k=int(input())
c=0
for i in range(n):
    if(l[i]==k):
        d=i
        c=1
        break
for i in range(n-1,-1,-1):
    if(l[i]==k):
        f=i
        c=1
        break
if(c==1):
    print(d,f)
else:
    print('-1 -1')