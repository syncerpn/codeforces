t = int(input())
for _ in range(t):
    a, b, c, d = list(map(int, input().strip().split(" ")))
    print("YES" if a == b == c == d else "NO")