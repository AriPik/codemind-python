x=input()
l=len(x)
k=0
for i in range(l):
    c=0
    for j in range(l):
        if x[i]==x[j] and i!=j:
            c=1
            break
    if(c==0):
        print(i)
        k=1
        break
if(k==0):
    print('-1')