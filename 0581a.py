a, b = list(map(int, input().strip().split(" ")))
m = min(a, b)
print(m, (max(a, b) - m) // 2)