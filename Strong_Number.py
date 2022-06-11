def fact(o):
    f=1
    for i in range(1,o+1):
        f*=i
    return f


n=int(input())
n1=n
su=0
while n!=0:
    r=n%10
    su=su+fact(r)
    n=n//10

if n1==su:
    print("The number",n1,"is a strong number")
else:
    print("The number",n1,"is not a strong number")