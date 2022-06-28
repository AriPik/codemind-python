def add(n):
    su=0
    if n==0:
        return 0
    elif  n>0 and n<10:
        su=su+n
    else:
        while(n!=0):
            r=n%10
            su=su+r
            n=n//10
    return su
n=int(input())
a=list(map(int,input().split()))[:n]
su=0
for i in range(len(a)):
    su=su+add(a[i])
print(su)