def fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

n=int(input())
while n:
    i=int(input())
    f=fact(i)
    print(f)
    n=n-1