n=int(input())
l=list(map(int,input().split()))[:n]
print(*set(l))