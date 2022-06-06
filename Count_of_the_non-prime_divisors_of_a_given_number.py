def prime(n):
    prime=True
    for i in range(2,n):
        if n%i==0:
            prime=False
            break
    if prime:
        return 1
    else:
        return 0
        
n=int(input())
c=0
for i in range(1,n+1):
    if n%i==0:
        if(prime(i)==0):
            c=c+1
print(c+1)