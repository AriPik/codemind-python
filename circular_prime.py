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
rev=0
if prime(n):
    while(n!=0):
        rem=n%10
        rev=rev*10+rem
        n=n//10
    if(prime(rev)):
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")