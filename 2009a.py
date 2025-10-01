t = int(input())
for _ in range(t):
    a, b = list(map(int, input().strip().split(" ")))
    print(b - a)