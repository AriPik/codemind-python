s1=input().lower()
s2=input().lower()
a=[]
b=[]
c=0
for i in s1.split():
    a.append(i)
for j in s2.split():
    b.append(j)
for i in range(len(a)):
    for j in range(len(b)):
        if a[i]==b[j]:
            c+=1
print(c)