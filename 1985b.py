t = int(input())
for _ in range(t):
    n = int(input())
    x = 2
    m, mx = 0, 2
    for x in range(2, n+1):
        k = n // x
        s = (1 + k) * k * x // 2
        if s > m:
            m, mx = s, x
    print(mx)