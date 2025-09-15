from collections import defaultdict
import random
RD = random.getrandbits(31)

t = int(input())
for _ in range(t):
    n, k = list(map(int, input().strip().split(" ")))
    A = list(map(int, input().strip().split(" ")))
    d = defaultdict(int)
    for a in A:
        d[a ^ RD] += 1
        
    for ak in d:
        if d[ak] % k != 0:
            print(0)
            break
        else:
            d[ak] //= k
    else:
        l = 0
        f = defaultdict(int)
        ans = 0
        for r, a in enumerate(A):
            f[a ^ RD] += 1
            while f[a ^ RD] > d[a ^ RD]:
                b = A[l]
                f[b ^ RD] -= 1
                l += 1
            ans += r - l + 1
        print(ans)