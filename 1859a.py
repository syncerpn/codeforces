t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().strip().split(" ")))
    m = min(A)
    B = []
    C = []
    for a in A:
        if a == m:
            B.append(a)
        else:
            C.append(a)
    if len(C) == 0:
        print(-1)
    else:
        print(len(B), len(C))
        print(" ".join(list(map(str, B))))
        print(" ".join(list(map(str, C))))