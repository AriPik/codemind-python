s=input()
a=s.split()
for i in a:
    m=ord(max(i))
    n=ord(min(i))
    print(abs(m-n),end=" ")