t = int(input())
for _ in range(t):
    s = input()
    n = len(s)
    p = -1
    ans = 0
    for i, c in enumerate(s):
        if c == "u":
            if p == i - 1:
                ans += 1
            else:
                p = i
    
    if p == n - 1:
        ans += 1
    print(ans)