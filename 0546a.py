k, n, w = list(map(int, input().strip().split(" ")))
print(max(0, (w + 1) * w // 2 * k - n))
