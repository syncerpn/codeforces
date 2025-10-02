t = int(input())
for _ in range(t):
    x = input()
    n = len(x)
    d = int(x[0])
    print((d - 1) * 10 + (1 + n) * n // 2)