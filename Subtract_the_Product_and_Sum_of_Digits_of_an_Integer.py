n=int(input())
n1=n
prod=1
su=0
while n!=0:
    rem=n%10
    su=su+rem
    n=n//10
    
while n1!=0:
    rem2=n1%10
    prod=prod*rem2
    n1=n1//10

res=prod-su
print(res)