t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip().split(" ")))
    b = list(map(int, input().strip().split(" ")))
    p = 0
    for ai, bi in zip(a, b):
        if ai > bi:
            p += ai - bi
    print(p + 1)