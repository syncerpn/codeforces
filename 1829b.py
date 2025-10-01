t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().strip().split(" ")))
    p = 0
    ans = 0
    for a in A:
        if a == 0:
            p += 1
            ans = max(ans, p)
        else:
            p = 0
    print(ans)