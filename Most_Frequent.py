n=int(input())
l=list(map(int,input().split()))[:n]
l1=[]
l2=[]
for i in l:
    if l.count(i) not in l1:
        l1.append(l.count(i))
m=max(l1)
for i in l:
    if l.count(i)==m:
        if i not in l2:
            l2.append(i)
if len(l2)==1:
    print(*l2)
else:
    print(min(l2))