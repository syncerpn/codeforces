t = int(input())
f = True
for _ in range(t):
    n = int(input())
    l, r = 0, n - 1
    
    d = list(map(int, input().strip().split(" ")))
    
    ans = ""
    while l < r:
        if (f and d[l] > d[r]) or (not f and d[l] < d[r]):
            ans += "LR"
        else:
            ans += "RL"
        r -= 1
        l += 1
        f = not f
    
    if l == r:
        ans += "L"
    print(ans)