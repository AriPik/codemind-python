n=int(input())
rev=0
rev1=0
sq=n**2
while n!=0:
    rem=n%10
    rev=rev*10+rem
    n=n//10

sq1=rev**2

while sq1!=0:
    rem1=sq1%10
    rev1=rev1*10+rem1
    sq1=sq1//10
    
if sq==rev1:
    print("True")
else:
    print("False")