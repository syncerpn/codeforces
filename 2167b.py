t = int(input())
for _ in range(t):
    n = int(input())
    s, r = input().strip().split(" ")
    print("YES" if sorted(s) == sorted(r) else "NO")