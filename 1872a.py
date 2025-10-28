t = int(input())
for _ in range(t):
    a, b, c = list(map(int, input().strip().split(" ")))
    d = abs(a - b)
    print(d // (c * 2) + (d % (c * 2) > 0))