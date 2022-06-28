def rev(m):
    rev=0
    while(m!=0):
        rem=m%10
        rev=rev*10+rem
        m=m//10
    return rev
n=int(input())
a=list(map(int,input().split()))[:n]
lst=[]
for i in range(len(a)):
    lst.append(rev(a[i]))
for i in range(len(lst)):
    print(lst[i],end=" ")