x=int(input())
for i in range(x):
    n=int(input())
    a=list(map(int,input().split()))
    if(sorted(a)==a):
        print('0')
    else:
        print(max(a)-min(a))