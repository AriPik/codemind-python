n=int(input())
while(n):
    n-=1
    x,y=map(int,input().split())
    a=list(map(int,input().split()))[:x]
    b=list(map(int,input().split()))[:y]
    l1=[]
    for i in a:
        l1.append(i)
    for i in b:
        l1.append(i)
    l1.sort()
    print(*l1)