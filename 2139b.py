t = int(input())
for _ in range(t):
    n, m = list(map(int, input().strip().split(" ")))
    A = list(map(int, input().strip().split(" ")))
    ans = 0
    A.sort(reverse=True)
    for i, a in enumerate(A):
        if i >= m:
            break
        ans += a * (m - i)
    print(ans)
        