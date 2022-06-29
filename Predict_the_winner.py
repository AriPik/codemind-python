n=int(input())
arr=list(map(int,input().strip().split()))
s1=0
s2=0
for i in range(n):
    if(i%2==0):
        s1=s1+arr[i]
    else:
        s2=s2+arr[i]
if(abs(s1-s2)%4==0):
    print("X")
else:
    print("Y")