from collections import Counter
import random
RD = random.getrandbits(31)
t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().strip().split(" ")))
    d = [Counter(), Counter()]
    m = [None] * 6
    k = 0
    ans = 0
    for i in range(n - 4):
        j = 1 - i % 2
        s = A[i] + A[i+2] - A[i+4]
        ss = s ^ RD
        ans += d[j][ss]
        ans += d[1-j][ss]
        if m[k-2] == s:
            ans -= 1
        if m[k-4] == s:
            ans -= 1
        d[1-j][ss] += 1
        m[k] = s
        k = (k + 1) % 6
    print(ans)