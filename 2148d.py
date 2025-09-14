t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().strip().split(" ")))
    s = []
    ans = 0
    for a in A:
        if a & 1:
            s.append(a)
        else:
            ans += a
    if not s:
        print(0)
    else:
        s.sort()
        m = len(s) // 2
        ans += sum(s[m:])
        print(ans)