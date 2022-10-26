n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
 
try:
    for i in range(m):
        a.remove(b[i])
    print('Yes')
except:
    print('No')