a,b=map(int,input().split())
if a==1 and b==10 or b==1 and a==10:
    print("Yes")
elif b==a+1 or a==b+1:
    print("Yes")
else:
    print("No")