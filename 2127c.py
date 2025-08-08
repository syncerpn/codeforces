import itertools
t = int(input())
for _ in range(t):
    n, k = list(map(int, input().strip().split(" ")))
    a = list(map(int, input().strip().split(" ")))
    b = list(map(int, input().strip().split(" ")))
    ans = 0
    for i in range(n):
        if a[i] < b[i]:
            a[i], b[i] = b[i], a[i]
        ans += a[i] - b[i]
    
    s = sorted((ai, bi) for ai, bi in zip(a, b))
    g = float("inf")
    for (ai, bi), (aj, bj) in itertools.pairwise(s):
        g = min(g, 2 * (bj - ai))
    ans += max(0, g)
    print(ans)