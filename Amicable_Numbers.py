m=int(input())
n=int(input())
c=0
d=0
for i in range(1,m):
    if m%i==0:
        c+=i
for j in range(1,n):
    if n%j==0:
        d+=j
        
if c==n and d==m:
    print("Amicable")
else:
    print("Not Amicable")