s1=input().lower()
s2=input().lower()
s1=s1.replace(" ","")
s2=s2.replace(" ","")
k=[]
for i in s1:
    if i in s2:
        k.append(i)
for i in s2:
    if i in s1:
        k.append(i)
k=set(k)
print(len(k))