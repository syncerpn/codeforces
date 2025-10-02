t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().strip().split(" ")))
    p = 0
    v = 0
    for i, a in enumerate(A):
        p += a % 2
        if (a % 2) != (i % 2):
            v += 1
    if p != n // 2:
        print(-1)
    else:
        print((v + 1) // 2)