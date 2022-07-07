n=int(input())
l=list(map(int,input().split()))[:n]
l1=[]
for i in l:
    l1.append(len(str(i)))
k=max(l1)
c=0
for j in range(len(l1)):
    if l1[j]==k:
        c+=1
print(c)