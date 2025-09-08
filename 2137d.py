# second time i got hacked again because of using dict
# we again need the trick
import collections
import random
RD = random.getrandbits(31)

t = int(input())
for _ in range(t):
    n = int(input())
    B = list(map(int, input().strip().split(" ")))
    S = collections.defaultdict(list)
    for i, b in enumerate(B):
        p = b ^ RD
        S[p].append(i)
    
    A = [""] * n
    j = 1
    for p in S:
        b = p ^ RD
        mb = len(S[p])
        if mb % b != 0:
            print(-1)
            break
        m = mb // b
        for ii, i in enumerate(S[p]):
            A[i] = str(j + ii % m)
        j += m
    else:
        print(" ".join(A))