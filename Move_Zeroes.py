x=int(input())
a=list(map(int,input().split()))
c=0
b=[]
for i in a:
    if(i!=0):
        b.append(i)
        c+=1
l=x-c
for i in range(l):
    b.append(0)
print(*b)