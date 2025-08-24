t = int(input())
for _ in range(t):
    n = int(input())
    g = list(map(int, input().strip().split(" ")))
    g.sort()
    i = len(g) - 1
    ans = 0
    while i >= 0:
        ans += g[i]
        i -= 2
    print(ans)