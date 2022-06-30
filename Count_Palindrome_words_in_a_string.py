s=input()
c=0
for i in s.split():
    if(i.lower()==i[::-1].lower()):
        c=c+1
print(c)        