n=int(input())
l=list(map(int,input().split()))[:n]
c=0
l1=[]
for i in l:
    i=str(abs(i))
    l1.append(len(i))
ma=max(l1)
for i in l1:
    if ma==i:
        c+=1
print(c)