t = int(input())
for _ in range(t):
    n = int(input())
    m, mi = 0, 0
    for i in range(n):
        a, b = list(map(int, input().strip().split(" ")))
        if a <= 10 and b > m:
            m = b
            mi = i + 1
    print(mi)