n=int(input())
l=list(map(int,input().split()))[:n]
s=0
for i in l:
    s=s*10+i
s=s+1
st=str(s)
print(*st)