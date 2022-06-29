x=int(input())
s=x*x
d=0
while(s>0):
    r=s%10
    d+=r
    s=s//10
if(d==x):
    print('Neon Number')
else:
    print('Not Neon Number')