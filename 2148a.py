t = int(input())
for _ in range(t):
    x, n = list(map(int, input().strip().split(" ")))
    print(x if n & 1 else 0)