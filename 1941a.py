t = int(input())
for _ in range(t):
    n, m, k = list(map(int, input().strip().split(" ")))
    A = list(map(int, input().strip().split(" ")))
    B = list(map(int, input().strip().split(" ")))
    A.sort()
    B.sort()
    j = m - 1
    ans = 0
    for i in range(n):
        while j >= 0 and B[j] + A[i] > k:
            j -= 1
        ans += j + 1
    print(ans)