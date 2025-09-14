t = int(input())
for _ in range(t):
    n = int(input())
    ans = [0]
    for _ in range(n):
        A = list(map(int, input().strip().split(" ")))
        if len(ans) == 1:
            ans += A
        else:
            ans.append(A[-1])
    ans[0] = n * (2 * n + 1) - sum(ans)
    print(" ".join(list(map(str, ans))))
    