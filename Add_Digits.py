def add_digits(num):
        return (num - 1) % 9 + 1 if num > 0 else 0

n=int(input())
print(add_digits(n))