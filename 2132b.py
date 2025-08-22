t = int(input())
for _ in range(t):
    n = int(input())
    i = 10
    c = 0
    xs = []
    while i + 1 <= n:
        if n % (i + 1) == 0:
            x = n // (i + 1)
            xs.append(x)
            c += 1
        i *= 10
    print(c)
    if c > 0:
        print(" ".join(list(map(str, sorted(xs)))))