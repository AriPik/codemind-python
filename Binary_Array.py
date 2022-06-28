n=int(input())
a=list(map(int,input().split()))[:n]
c=0
for i in range(len(a)):
    if a[i]==1 or a[i]==0:
        c+=1
if c==len(a):
    print("True")
else:
    print("False")