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
c=0
su=0
for i in range(0,len(a)):
    if prime(a[i]) and a[i]!=1:
        su+=a[i]
        c+=1
avg=su/c
print("%.2f"%avg)