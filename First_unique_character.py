s=input().lower().replace(" ","")
d=[]
for i in s:
    if s.count(i)==1:
        d.append(i)
if len(d)==0:
    print("-1")
else:
    print(d[0])