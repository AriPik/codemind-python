s=input().lower()
a=s.split()
c=0
v=['a','e','i','o','u']
l=[]
for i in a:
    c=0
    for j in i:
        if j in v:
            c+=1
    l.append(c)
ma=max(l)
print(l.count(ma))