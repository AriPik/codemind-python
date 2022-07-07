n=int(input())
l=list(map(int,input().split()))
if sorted(l,reverse=True)==l:
    print("yes")
else:
    print("no")