t = int(input())
for _ in range(t):
    a, b = list(map(int, input().strip().split(" ")))
    if a == b:
        print(0)
    else:
        a, b = max(a, b), min(a, b)
        if a % b == 0:
            print(1)
        else:
            print(2)
    