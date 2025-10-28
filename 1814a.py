t = int(input())
for _ in range(t):
    n, k = list(map(int, input().strip().split(" ")))
    if n % 2 and k % 2 == 0:
        print("NO")
    else:
        print("YES")