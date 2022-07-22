n=int(input())
l=list(map(int,input().split()))[:n]
l1=[]
for i in l:
    l1.append(len(str(abs(i))))
m=max(l1)
for i in l:
    if len(str(abs(i)))==m:
        print(i,end=" ")