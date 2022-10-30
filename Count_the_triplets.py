t=int(input())
for k in range(t):
    n=int(input())
    c=0
    l=list(map(int,input().split()))
    ll=list(set(l))
    for i in range(n-1):
        for j in range(i+1,n):
            s=l[i]+l[j]
            if s in ll:
                c+=1
    if c==0:
        print("-1")
    else:
        print(c)