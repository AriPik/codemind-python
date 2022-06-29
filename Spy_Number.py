x=int(input())
s,p=0,1
while(x>0):
    r=x%10
    s+=r
    p*=r
    x=x//10
if(s==p):
    print('Spy Number')
else:
    print('Not Spy Number')