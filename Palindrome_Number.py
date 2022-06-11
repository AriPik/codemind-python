n=int(input())
while n:
    a=int(input())
    at=a
    rev=0
    while(a!=0):
        rem=a%10
        rev=rev*10+rem
        a=a//10
    if at==rev:
        print("True")
    else:
        print("False")
    n=n-1