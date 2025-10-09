from itertools import pairwise
t = int(input())
for _  in range(t):
    n = int(input())
    S = list(map(int, input().strip().split(" ")))
    S.sort()
    m = float("inf")
    for a, b in pairwise(S):
        m = min(m, b-a)
    print(m)