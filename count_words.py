s=input().lower()
a=s.split()
c1=0
v=['a','e','i','o','u']
c=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
for i in a:
    l=len(i)
    if i[0] in v and i[l-1] in c:
        c1+=1
print(c1)