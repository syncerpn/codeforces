t = int(input())
for _ in range(t):
    x, y, r = list(map(int, input().strip().split(" ")))
    print(x, y - r)