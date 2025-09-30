l = 1
dp = []
for _ in range(1000):
    while (l - 3) % 10 == 0 or l % 3 == 0:
        l += 1
    dp.append(l)
    l += 1

t = int(input())
for _ in range(t):
    print(dp[int(input()) - 1])
    