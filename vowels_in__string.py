s=input()
v=['a','e','i','o','u','A','E','I','O','U']
k=[]
for i in s:
    if i in v and i not in k:
        k.append(i)
for j in k:
    print(j,end=" ")