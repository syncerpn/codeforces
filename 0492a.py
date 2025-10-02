n = int(input())
x = 1
while x * (x + 1) * (x + 2) <= 6 * n:
    x += 1
print(x - 1)