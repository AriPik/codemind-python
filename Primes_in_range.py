def prime(n):
    prime=True
    if(n==1):
        return 0
    if n==2:
        return 1
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                prime=False
                break
    if prime:
        return 1
    else:
        return 0
m=int(input())
n=int(input())
c=0
for i in range(m,n+1):
    if prime(i):
        c+=1
print(c)