t = int(input())
for _ in range(t):
    n = int(input())
    if n % 2:
        ans = [-1, 3] * ((n-1) // 2) + [-1]
    else:
        ans = [-1, 3] * ((n-2) // 2) + [-1, 2]
    print(" ".join(list(map(str, ans))))