t = int(input())
for _ in range(t):
    n = int(input())
    if n & 1:
        print(n, end=" ")
        for i in range(1, n-1):
            print(i, end=" ")
        print(n-1)

    else:
        print(-1)