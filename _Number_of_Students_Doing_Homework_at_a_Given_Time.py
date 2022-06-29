x=int(input())
a=list(map(int,input().split()))
y=int(input())
b=list(map(int,input().split()))
c=int(input())
s=0
for i in range(x):
    if c>=a[i] and c<=b[i]:
        s+=1
print(s)