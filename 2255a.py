t = int(input())
for _ in range(t):
    n, k = list(map(int, input().strip().split(" ")))
    s = input()
    n <<= 1
    r, b = 0, 0
    for i, a in enumerate(s):
        if a == "1":
            if s[(i+1) % n] == "1":
                if i % 2:
                    r += 1
                else:
                    b += 1
            else:
                if i % 2:
                    b += 1
                else:
                    r += 1
    print(r, b)