# -*- coding: utf-8 -*-
"""
Created on Mon Aug 25 08:43:23 2025

@author: nghia
"""

t = int(input())
for _ in range(t):
    n = int(input())
    h = list(map(int, input().split()))
    dp = [0] * (n + 1)
    dp[1] = h[0]
    for i in range(1, n):
        dp[i + 1] = min(dp[i] + h[i] - 1, dp[i - 1] + h[i - 1] + max(0, h[i] - i))
    print(dp[n])