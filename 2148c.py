t = int(input())
for _ in range(t):
    n, m = list(map(int, input().strip().split(" ")))
    s, p = 0, 0
    ans = 0
    for _ in range(n):
        r, q = list(map(int, input().strip().split(" ")))
        if r & 1 == s & 1:
            ans += r - s - (p != q)
        else:
            ans += r - s - (p == q)
        s, p = r, q
    ans += m - s
    print(ans)