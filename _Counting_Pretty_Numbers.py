n=int(input())
while n:
    c=0
    a,b=map(int,input().split())
    for i in range(a,b+1):
        rem=i%10
        if rem==2 or rem==3 or rem==9:
            c=c+1
        i=i/10
    print(c)
    n=n-1