t = int(input())
for _ in range(t):
    a, b = list(map(int, input().strip().split(" ")))
    if b > a:
        if (b - a) % 2 == 1:
            print(1)
        else:
            print(2)
    elif b < a:
        if (b - a) % 2 == 1:
            print(2)
        else:
            print(1)
    else:
        print(0)