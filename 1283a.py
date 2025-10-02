t = int(input())
for _ in range(t):
    h, m = list(map(int, input().strip().split(" ")))
    print((24 - h) * 60 - m)