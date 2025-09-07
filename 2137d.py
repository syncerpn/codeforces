t = int(input())
for _ in range(t):
    n = int(input())
    B = list(map(int, input().strip().split(" ")))
    S = {}
    dp = [0] * (n + 1)
    for i, b in enumerate(B):
        dp[b] += 1
        if b not in S:
            S[b] = []
        S[b].append(i)
    
    A = [""] * n
    j = 1
    for b in S:
        if dp[b] % b != 0:
            print(-1)
            break
        m = dp[b] // b
        for ii, i in enumerate(S[b]):
            A[i] = str(j + ii % m)
        j += m
    else:
        print(" ".join(A))