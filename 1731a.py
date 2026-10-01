t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().strip().split(" ")))
    p = 1
    for a in A:
        p *= a
    print((p + n - 1) * 2022)