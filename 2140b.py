t = int(input())
for _ in range(t):
    x = int(input())
    k = 10
    while x >= k - 1 or (k - 1 - x) * 10 < k:
        k *= 10
    print(k - 1 - x)

# editorial: y = 2 * x
t = int(input())
for _ in range(t):
    x = int(input())
    print(2 * x)