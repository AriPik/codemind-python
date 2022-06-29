def pal(n):
    s=0
    temp=n
    while(n!=0):
        d=n%10
        s=s*10+d
        n=n//10
    if(s==temp):
        return 1
    else:
        return 0
def prime(n):
    c=0
    for i in range(1,n+1):
        if(n%i==0):
            c=c+1
    if(c==2):
        return 1
    else:
        return 0
n=int(input())
a=n+1
while(1):
    if(pal(a) and prime(a)):
        k=a
        break
    a=a+1
print(k)    
        