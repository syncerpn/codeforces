t = int(input())
for _ in range(t):
    n, m = list(map(int, input().strip().split(" ")))
    x = input()
    s = input()
    if s in x:
        print(0)
        continue
    x += x
    n *= 2
    ans = 1
    while n <= 2 * m:
        if s in x:
            print(ans)
            break
        x += x
        n *= 2
        ans += 1
    else:
        if s in x:
            print(ans)
        else:
            print(-1)
        