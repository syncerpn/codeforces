t = int(input())
for _ in range(t):
    n = int(input())
    s = input().split("#")
    ans = 0
    g = False
    for c in s:
        if len(c) >= 3:
            print(2)
            break
        ans += len(c)
    else:
        print(ans)