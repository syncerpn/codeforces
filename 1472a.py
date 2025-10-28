t = int(input())
for _ in range(t):
    w, h, n = list(map(int, input().strip().split(" ")))
    s = w * h
    ans = 1
    while ans < n:
        if s % 2:
            print("NO")
            break
        s //= 2
        ans *= 2
    else:
        print("YES")
        