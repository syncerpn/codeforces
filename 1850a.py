t = int(input())
for _ in range(t):
    a, b, c = list(map(int, input().strip().split(" ")))
    print("YES" if a + b + c - min(a, b, c) >= 10 else "NO")