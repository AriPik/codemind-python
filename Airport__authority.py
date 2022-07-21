n=int(input())
l=[]
while(n):
    n-=1
    i=int(input())
    l.append(i)
t=int(input())
c=0
for i in range(len(l)):
    if l[i]<=t:
        c+=1
    if l[i]>t:
        c+=2
print(c)