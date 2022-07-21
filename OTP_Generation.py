s=input()
a=[]
s1=""
for i in s:
    a.append(int(i))
for j in range(len(a)):
    if a[j]%2!=0 and a[j]!=0:
        s1+=str(a[j]**2)
print(s1)