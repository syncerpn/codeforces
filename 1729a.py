t = int(input())
for _ in range(t):
    a, b, c = list(map(int, input().strip().split(" ")))
    df = a - 1
    ds = abs(c - b) + abs(c - 1)
    if df == ds:
        print(3)
    else:
        print(1 if ds > df else 2)