def prime(n):
    p=True
    for i in range(2,n):
        if n%i==0:
            p=False
            break
    if p:
        return 1
    else:
        return 0
def reverse(n):
    rev=0
    while(n!=0):
        rem=n%10
        rev=rev*10+rem
        n=n//10
    return rev
n=int(input())
if prime(n):
    if prime(reverse(n)):
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")