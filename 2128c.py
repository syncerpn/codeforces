t = int(input())
for _ in range(t):
    n = int(input())
    d = list(map(int, input().strip().split(" ")))
    m = float("inf")
    for a in d:
        if a >= 2 * m:
            print("no")
            break
        m = min(m, a)
    else:
        print("yes")