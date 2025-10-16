from itertools import pairwise
t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().strip().split(" ")))
    m = float("inf")
    for a, b in pairwise(A):
        m = min(m, b-a)
    
    print(max(0, 1 + m // 2))