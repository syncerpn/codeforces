import math
t = int(input())
for _ in range(t):
    a, b = list(map(int, input().strip().split(" ")))
    print(int(math.ceil(abs(b - a) / 10)))