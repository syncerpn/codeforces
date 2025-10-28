n, m, k = list(map(int, input().strip().split(" ")))
print("YES" if min(m, k) >= n else "NO")
