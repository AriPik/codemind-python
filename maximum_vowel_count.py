s=input().lower()
a=s.split()
c=0
ma=0
v=['a','e','i','o','u']
for i in a:
    c=0
    for j in i:
        if j in v:
            c+=1
        if ma<c:
            ma=c
print(ma)