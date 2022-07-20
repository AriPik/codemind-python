s=input().lower()
k=s.split()
l=[]
c=0
v=['a','e','i','o','u']
for i in k:
    c=0
    for j in i:
        if j in v:
            c+=1
    l.append(c)
print(min(l))