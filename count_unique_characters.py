s=input().lower().replace(" ","")
c=0
for i in s:
    k=s.count(i)
    if k==1:
        c+=1
print(c)