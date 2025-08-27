t = int(input())
for _ in range(t):
    n, a, b = list(map(int, input().strip().split(" ")))
    if ((n - b) % 2 == 0) and ((a < b) or ((a - b) % 2 == 0)):
        print("YES")
    else:
        print("NO")