n1=int(input())
n2=int(input())
su=0
su1=0
for i in range(1,n1):
    if n1%i==0:
        su=su+i
for j in range(1,n2):
    if n2%j==0:
        su1=su1+j
if su==n2 and su1==n1:
    print("Amicable")
else:
    print("Not Amicable")