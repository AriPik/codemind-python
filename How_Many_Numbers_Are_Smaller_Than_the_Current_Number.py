n=int(input())
a=list(map(int,input().split()))[:n]
c=0
for i in a:
    c=0
    for j in a:
        if j!=i and j<i:
            c+=1
    print(c,end=" ")