n=int(input())
l=list(map(int,input().split()))[:n]
l1=[]
for i in l:
    s=l.count(i)
    if s>1:
        if i not in l1:
            l1.append(i)
print(*l1)