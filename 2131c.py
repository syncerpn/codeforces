# first time learned that python's built-in dict can easily be hacked
# making the runtime O(n2)
import collections
import random
RD = random.getrandbits(31)

t = int(input())
for _ in range(t):
    n, k = list(map(int, input().strip().split(" ")))
    s = list(map(int, input().strip().split(" ")))
    t = list(map(int, input().strip().split(" ")))
    d = collections.defaultdict(int)
    for a in t:
        p = min((k - a) % k, a % k) ^ RD
        d[p] += 1
    
    for a in s:
        p = min((k - a) % k, a % k) ^ RD
        d[p] -= 1
        if d[p] < 0:
            print("NO")
            break
    else:
        print("YES")