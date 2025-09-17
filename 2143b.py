from itertools import accumulate
t = int(input())
for _ in range(t):
    n, k = list(map(int, input().strip().split(" ")))
    A = list(map(int, input().strip().split(" ")))
    B = list(map(int, input().strip().split(" ")))
    A.sort(reverse=True)
    B = set(accumulate(sorted(B)))
    ans = 0
    for i, a in enumerate(A):
        if i+1 in B:
            continue
        ans += a
    print(ans)