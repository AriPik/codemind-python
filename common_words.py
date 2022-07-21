s1=input().lower().split()
s2=input().lower().split()
c=0
for i in s2:
    if i in s1:
        c=1
        print(i,end=" ")