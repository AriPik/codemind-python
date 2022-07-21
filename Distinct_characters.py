s=input().lower().replace(" ","")
d=[]
for i in s:
    if s.count(i)==1:
        d.append(i)
d.sort()
for i in d:
    print(i,end="")