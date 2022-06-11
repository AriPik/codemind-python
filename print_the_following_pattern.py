size = int(input())

for i in range(size):
    for j in range(size):
        print(chr(65 + i), end=" ")
    print()