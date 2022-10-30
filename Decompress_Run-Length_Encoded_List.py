n=int(input())
l=list(map(int,input().split()))
t=[]
k=[]
for i in range(n):
    if i%2==0:
        t.append(l[i])
    else:
        k.append(l[i])
f=[]
for i in range(len(k)):
    for j in range(t[i]):
        f.append(k[i])
print(*f)