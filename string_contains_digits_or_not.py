n=int(input())
while(n):
    n-=1
    c=0
    s=input()
    d=['0','1','2','3','4','5','6','7','8','9']
    for i in s:
        if i in d:
            c+=1
    if c!=0:
        print("Yes")
    else:
        print("No")