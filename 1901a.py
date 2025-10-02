t = int(input())
for _ in range(t):
    n, x = list(map(int, input().strip().split(" ")))
    A = list(map(int, input().strip().split(" ")))
    p = 0
    ans = 0
    for a in A:
        ans = min(ans, p - a)
        p = a
    ans = min(ans, 2 * (p - x))
    print(-ans)