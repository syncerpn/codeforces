t = int(input())
for _ in range(t):
    s = input()
    n = int(s)
    l = len(s)
    ans = (len(s) - 1) * 9
    k = int("1" * l)
    for i in range(1, 10):
        if k * i > n:
            print(ans + i - 1)
            break
    else:
        print(ans + 9)