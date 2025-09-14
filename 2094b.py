t = int(input())
for _ in range(t):
    n, m, l, r = list(map(int, input().strip().split(" ")))
    d = n - m
    if r >= d:
        print(l, r - d)
    else:
        k = d - r
        print(l + k, 0)
