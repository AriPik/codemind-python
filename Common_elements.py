a,b=map(int,input().split())
k=list(map(int,input().split()))[:a]
l=list(map(int,input().split()))[:b]
m=[]
n=[]
for i in k:
   if i not in m:
       m.append(i)
for j in l:
    if j not in n:
        n.append(j)
for p in m:
    if p in n:
        print(p,end=" ")