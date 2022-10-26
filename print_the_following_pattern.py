x=int(input())
for i in range(x,0,-1):
    for j in range(i):
        print(chr(i+64),end=" ")
    print()