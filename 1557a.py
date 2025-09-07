t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().strip().split(" ")))
    s = sum(A)
    m = max(A)
    print((s-m)/(n-1) + m)