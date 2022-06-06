def palindrome(n):
    n1=n
    rev=0
    while(n!=0):
        rem=n%10
        rev=rev*10+rem
        n=n//10
    if n1==rev:
        return 1
    else:
        return 0
m=int(input())
n=int(input())
for i in range(m,n):
    if palindrome(i)==1:
        print(i,end=" ")