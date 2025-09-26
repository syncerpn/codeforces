t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    a = []
    b = []
    for i, c in enumerate(s):
        if c == "a":
            a.append(i)
        else:
            b.append(i)
    
    ans = float("inf")
    for q in [a, b]:
        k = len(q)
        l = [0]
        for ii, i in enumerate(q):
            l.append(i - ii + l[-1])
        
        r = 0
        ans = min(ans, l[k])
        for ii in range(k - 1, -1, -1):
            i = q[ii]
            r += n - k + ii - i
            ans = min(ans, l[ii] + r)
    print(ans)