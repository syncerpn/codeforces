from itertools import pairwise
t = int(input())
for _ in range(t):
    n = int(input())
    A = sorted(list(map(int, input().strip().split(" "))))
    for a, b in pairwise(A):
        if b - a > 1:
            print("NO")
            break
    else:
        print("YES")