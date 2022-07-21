s=input().replace(" ","")
a=min(s)
b=max(s)
c1=0
c2=0
if a.isalpha() or a.isnum():
    if b.isalpha() or b.isnum():
        for i in s:
            if i==a:
                c2+=1
            if i==b:
                c1+=1
print(a,c2,b,c1)