t = int(input())
for _ in range(t):
    a, b, n = list(map(int, input().strip().split(" ")))
    if a > b:
        a, b = b, a
    ans = 0
    while b <= n:
        a, b = b, a + b
        ans += 1
    print(ans)