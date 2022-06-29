x,y=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=0
d=[]
for i in a:
    if i in b:
        d.append(i)
print(len(set(d)))