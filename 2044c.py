t = int(input())
for _ in range(t):
    m, a, b, c = list(map(int, input().strip().split(" ")))
    e = min(c, m - min(a, m) + m - min(b, m))
    print(e + min(a, m) + min(b, m))