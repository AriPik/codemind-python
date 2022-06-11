num=int(input())
ma=0
while num>0:
    digit=num%10
    if ma<digit:
        ma=digit
    num=num//10
print(ma)