t = int(input())
for _ in range(t):
    l, r, d, u = list(map(int, input().strip().split(" ")))
    print("YES" if l == r and r == d and d == u else "NO")