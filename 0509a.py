n = int(input())
dp = [[1 for _ in range(n)] for _ in range(n)]
for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
print(dp[-1][-1])