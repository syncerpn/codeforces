t = int(input())
for _ in range(t):
    n = int(input())
    ans = 0
    i, j = 0, 1
    while n > 0:
        m = n % 3
        ans += m * (j * 3 + i * j // 3)
        n //= 3
        i += 1
        j *= 3
    print(ans)
            