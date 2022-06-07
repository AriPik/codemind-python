n=int(input())
n1=n
s=0
for i in range(1,n):
    if n%i==0:
        s=s+i
if s==n1:
    print("True")
else:
    print("False")