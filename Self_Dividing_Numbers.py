def selfdividing(n):
    if n<10:
        return 1
    if n%10==0:
        return 0
    t=n
    fg=0
    while(n!=0):
        r=n%10
        if t%r!=0:
            fg=1
            break
        n=n//10
    if fg==0:
        return 1
    else:
        return 0

l=int(input())
r=int(input())
for i in range(l,r+1):
    if selfdividing(i):
        print(i,end=" ")