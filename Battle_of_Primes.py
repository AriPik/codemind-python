x=int(input())
y=int(input())
z=x+y
s=0
while(1):
    z=z+1
    c=0
    for i in range(1,z+1):
        if(z%i==0):
            c+=1
    if(c==2):
        print(s+1)
        break
    else:
        s+=1