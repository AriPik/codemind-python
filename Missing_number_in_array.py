n=int(input())
while n:
    n-=1
    j=int(input())
    l=list(map(int,input().split()))[:j-1]
    for i in range(1,j+1):
        if i not in l:
            print(i)