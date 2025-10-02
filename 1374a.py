t = int(input())
for _ in range(t):
    x, y, n = list(map(int, input().strip().split(" ")))
    print((n - y) // x * x + y)