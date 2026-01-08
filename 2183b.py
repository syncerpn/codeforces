t = int(input())
for _ in range(t):
    n, k = list(map(int, input().strip().split(" ")))
    A = list(map(int, input().strip().split(" ")))
    dp = [False] * (k - 1)
    for a in A:
        if a < k - 1:
            dp[a] = True
    
    for a in range(k - 1):
        if not dp[a]:
            print(a)
            break
    else:
        print(k - 1)