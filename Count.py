n=int(input())
l=list(map(int,input().split()))[:n]
c_o=0
c_e=0
for i in l:
    if i%2==0:
        c_e+=1
    else:
        c_o+=1
print(c_e,c_o)