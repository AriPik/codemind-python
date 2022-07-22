def maxi(l):
    if len(l)<=2:
        return max(l)
    elif len(l)>=3:
        l.remove(max(l))
        l.remove(max(l))
    return max(l)
n=int(input())
l=list(map(int,input().split()))
k=set(l)
print(maxi(k))