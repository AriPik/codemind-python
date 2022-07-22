n=int(input())
l=list(map(int,input().split()))[:n]
l1=[]
for i in l:
    l1.append(i**2)
l1.sort()
print(*l1)