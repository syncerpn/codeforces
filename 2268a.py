t = int(input())
for _ in range(t):
    n, k = list(map(int, input().strip().split(" ")))
    A = list(map(int, input().strip().split(" ")))
    ans = 0
    r = k - 1
    l = n - 1 - r
    if r <= l:
        ans += sum(A[r:l+1])
        l, r = r - 1, l + 1
    while l >= 0:
        ans += max(A[l], A[r])
        l -= 1
        r += 1
    print(ans)