n=int(input())
l=list(map(int,input().split()))[:n]
l1=[]
for i in l:
    if l.count(i)==1:
        l1.append(i)
if len(l1)==0:
    print("-1")
else:
    for i in l1:
        print(i,end=" ")