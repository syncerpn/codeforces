from itertools import pairwise
n = int(input())
A = list(map(int, input().strip().split(" ")))
ans = 1
l = 1
for a, b in pairwise(A):
    if b > a:
        l += 1
        ans = max(ans, l)
    else:
        l = 1
print(ans)