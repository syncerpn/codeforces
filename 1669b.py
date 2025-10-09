import collections
import random
RD = random.getrandbits(31)

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().strip().split(" ")))
    d = collections.defaultdict(int)
    for a in A:
        p = a ^ RD
        d[p] += 1
        if d[p] == 3:
            print(a)
            break
    else:
        print(-1)