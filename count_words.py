s=input()
s=s.lower()
n=s.split()
l=len(n)
x=0
v=['a','e','i','o','u']
c=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
for i in range(0,l):
    k=n[i]
    s1=len(k)
    if k[0] in v and k[s1-1] in c:
        x+=1
print(x)