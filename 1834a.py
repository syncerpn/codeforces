t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().strip().split(" ")))
    p, q = A.count(-1), A.count(1)
    ans = 0
    if p % 2:
        ans += 1
        p -= 1
        q += 1
    if q < p:
        ans += ((p - q + 1) // 2 + 1) // 2 * 2
    print(ans)