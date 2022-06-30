def pal(n):
    temp=n
    s=0
    while(n!=0):
        d=n%10
        s=s*10+d
        n=n//10
    if(s==temp):
        return 1
    else:
        return 0
n=int(input())
arr=list(map(int,input().split()))
c=0
for i in range(len(arr)):
    if(pal(arr[i])):
        c=c+1
print(c)        