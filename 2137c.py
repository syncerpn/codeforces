t = int(input())
for _ in range(t):
    a, b = list(map(int, input().strip().split(" ")))
    if a & 1 and b & 1:
        print(a*b + 1)
    elif b & 1:
        print(-1)
    elif a & 1:
        if (b // 2) & 1:
            print(-1)
        else:
            print(a*b//2+2)
    else:
        print(a*b//2 + 2)