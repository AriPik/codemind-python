n=int(input())
a=list(map(int,input().split()))[:n]
c=0
for i in range(len(a)):
    if i%2!=0:
        c+=a[i]
print(c)