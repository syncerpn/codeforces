import bisect

t = int(input())
for _ in range(t):
    n, c = list(map(int, input().strip().split(" ")))
    d = list(map(int, input().strip().split(" ")))
    d.sort()
    j = n
    while n and j:
        i = bisect.bisect(d, c, hi=j)
        if i == 0:
            break
        c /= 2
        j = min(j - 1, i - 1)
        n -= 1
    print(n)