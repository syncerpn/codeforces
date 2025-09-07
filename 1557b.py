from itertools import pairwise
t = int(input())
for _ in range(t):
    n, k = list(map(int, input().strip().split(" ")))
    A = list(map(int, input().strip().split(" ")))
    A = sorted([(a, i) for i, a in enumerate(A)])
    c = 1
    for ai, bj in pairwise(A):
        a, i = ai
        b, j = bj
        if j != i + 1:
            c += 1
    print("YES" if c <= k else "NO")