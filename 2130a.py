t = int(input())
for _ in range(t):
    n = int(input())
    d = list(map(int, input().strip().split(" ")))
    ans = 0
    for a in d:
        ans += max(a, 1)
    print(ans)