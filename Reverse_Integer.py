def rev(n):
    su=0
    while n!=0:
        r=n%10
        su=su*10+r
        n//=10
    return su
n=int(input())
su=0
if n>0:
    print(rev(n))
else:
    n=-n
    print(-(rev(n)))