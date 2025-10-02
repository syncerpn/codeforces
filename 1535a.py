t = int(input())
for _ in range(t):
    a, b, c, d = list(map(int, input().strip().split(" ")))
    print("NO" if max(a, b) < min(c, d) or max(c, d) < min(a, b) else "YES")