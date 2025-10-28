t = int(input())
for _ in range(t):
    n, k = list(map(int, input().strip().split(" ")))
    A = list(map(int, input().strip().split(" ")))
    r = 0
    ans = 0
    for a in A:
        if a >= k:
            r += a
        elif a == 0:
            if r > 0:
                r -= 1
                ans += 1
    print(ans)