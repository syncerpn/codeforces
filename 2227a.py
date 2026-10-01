t = int(input())
for _ in range(t):
    a, b = list(map(int, input().strip().split(" ")))
    print("NO" if a & 1 and b & 1 else "YES")