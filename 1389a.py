t = int(input())
for _ in range(t):
    l, r = list(map(int, input().strip().split(" ")))
    if l * 2 <= r:
        print(l, l * 2)
    else:
        print(-1, -1)