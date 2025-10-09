t = int(input())
for _ in range(t):
    n, a, b = list(map(int, input().strip().split(" ")))
    if b < a * 2:
        print((n // 2) * b + (n % 2) * a)
    else:
        print(n * a)