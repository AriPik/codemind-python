n=int(input())
a=list(map(int,input().split()))[:n]
su_odd=0
su_even=0
for i in range(len(a)):
    if i%2==0:
        su_even+=a[i]
    else:
        su_odd+=a[i]
diff=su_odd-su_even
if diff==0:
    print("YES")
else:
    print("NO")