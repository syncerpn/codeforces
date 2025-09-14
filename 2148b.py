import bisect
t = int(input())
for _ in range(t):
    n, m, x, y = list(map(int, input().strip().split(" ")))
    Y = list(map(int, input().strip().split(" ")))
    X = list(map(int, input().strip().split(" ")))
    xi = bisect.bisect(X, x)
    yi = bisect.bisect(Y, y)
    print(xi + yi)