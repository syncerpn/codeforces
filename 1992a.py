t = int(input())
for _ in range(t):
    a, b, c = list(map(int, input().strip().split(" ")))
    for _ in range(5):
        if a <= b:
            if a <= c:
                a += 1
            else:
                c += 1
        else:
            if b <= c:
                b += 1
            else:
                c += 1
    print(a * b * c)