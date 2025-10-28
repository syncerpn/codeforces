t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().strip().split(" ")))
    s = []
    for i, a in enumerate(A):
        if a == 2:
            s.append(i)
    if not s:
        print(1)
    elif len(s) % 2 == 0:
        print(s[len(s) // 2 - 1] + 1)
    else:
        print(-1)