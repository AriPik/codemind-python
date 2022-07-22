n=int(input())
s=0
i=0
while(s<=n):
    s=pow(2,i)
    i=i+1
l=s//2
x=abs(n-s)
y=abs(n-l)
if x>y:
    print(y)
else:
    print(x)