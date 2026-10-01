t = int(input())
for _ in range(t):
    n, k = list(map(int, input().strip().split(" ")))
    m = n - k + 1
    print(2 * (k - 1) + (1 << m))