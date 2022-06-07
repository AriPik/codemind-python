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
n1=int(input())
n2=int(input())
for i in range(n1,n2):
   if i!=1:
       if(prime(i)):
           print(i)