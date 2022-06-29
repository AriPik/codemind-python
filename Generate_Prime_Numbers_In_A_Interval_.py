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

m=int(input())
n=int(input())
for i in range(m,n):
    if prime(i) and i!=1:
        print(i)