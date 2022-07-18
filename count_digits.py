n=int(input())
l=list(map(int,input().split()))[:n]
l1=[]
for i in l:
    i=str(abs(i))
    l1.append(len(i))
print(*l1)