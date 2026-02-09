n, m = list(map(int, input().strip().split(" ")))

d = n - m
if m == n:
    if m == 1:
        print(2)
    else:
        a = int((m + 1 / 4) ** 0.5 - 1/2)
        if a * a + a == m:
            print(1)
        else:
            print(0)
else:
    ans = 0
    for p in range(-abs(d), abs(d) + 1):
        if p and d % p == 0:
            q = d // p
            if p % 2 != q % 2:
                a = (p + q + 1) // 2
                if a >= 0:
                    b = a - p
                    if b >= 0 and (a * a + b == n) and (a + b * b == m):
                        ans += 1
    print(ans)