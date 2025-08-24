# -*- coding: utf-8 -*-
"""
Created on Tue Jun 24 20:48:35 2025

@author: nghia
"""
import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split(" ")))

import collections

d = collections.Counter(nums)

dp = [{}, {}]
s = sorted(d.keys())

for i, a in enumerate(s):
    if i == 0:
        dp[0][a] = 0
        dp[1][a] = d[a] * a
    elif i == 1:
        b = s[i-1]
        if b != a - 1:
            dp[1][a] = dp[1][b] + d[a] * a
        else:
            dp[1][a] = dp[0][b] + d[a] * a
        dp[0][a] = dp[1][b]
    else:
        b, c = s[i-1], s[i-2]
        if b == a - 1:
            dp[1][a] = max(dp[1][c], dp[0][b]) + d[a] * a
        else:
            dp[1][a] = max(dp[1][b], dp[0][b]) + d[a] * a
        dp[0][a] = max(dp[1][b], dp[0][b])
        
print(max(dp[0][s[-1]], dp[1][s[-1]]))