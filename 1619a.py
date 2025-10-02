t = int(input())
for _ in range(t):
    s = input()
    n = len(s)
    print("YES" if s[:n//2] == s[n//2:] else "NO")