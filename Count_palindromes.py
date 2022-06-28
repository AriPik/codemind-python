def palindrome(n):
    x=n
    rev=0
    while(n!=0):
        rem=n%10
        rev=rev*10+rem
        n=n//10
    if x==rev:
        return 1
    else:
        return 0
n=int(input())
a=list(map(int,input().split()))[:n]
c=0
for i in range(len(a)):
    if palindrome(a[i]):
        c+=1
print(c)