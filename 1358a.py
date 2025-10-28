t = int(input())
for _ in range(t):
    n, m = list(map(int, input().strip().split(" ")))
    l = n * m
    print(l // 2 + l % 2)