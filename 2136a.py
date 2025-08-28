t = int(input())
for _ in range(t):
    a, b, c, d = list(map(int, input().strip().split(" ")))
    c -= a
    d -= b
    a, b = max(a, b), min(a, b)
    if a - 2 > 2 * b:
        print("NO")
        continue
    a, b = max(c, d), min(c, d)
    if a - 2 > 2 * b:
        print("NO")
        continue
    print("YES")
    