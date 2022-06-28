def prime(n):
    prime=True
    for i in range(2,n):
        if n%i==0:
            prime=False
            break
    if prime:
        return 1
    else:
        return 0
n=int(input())
a=list(map(int,input().split()))[:n]
k=int(input())
c=0
for i in range(len(a)):
    if prime(a[i]):
        if a[i]>=k:
            c+=1
print(c)