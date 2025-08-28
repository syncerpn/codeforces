from collections import deque
t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().strip().split(" ")))
    m = max(A)
    s = [deque() for _ in range(m+1)]
    dp = [0] * (n + 1)
    for i, a in enumerate(A):
        s[a].append(i)
        dp[i+1] = dp[i]
        if len(s[a]) >= a:
            dp[i+1] = max(dp[i+1], dp[s[a].popleft()] + a)
    
    print(dp[n])
    