s1=input().lower().replace(' ',"")
s2=input().lower().replace(' ',"")
c=""
d=1
for i in s1:
    if i not in s2:
        c+=i
for i in s2:
    if i not in s1:
        c+=i
s=list(set(c))
s.sort()
for k in s:
    print(k,end="")