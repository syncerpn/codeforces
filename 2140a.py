t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    k = s.count("0")
    ans = 0
    for i, c in enumerate(s):
        if c == "0" and i >= k:
            ans += 1
    print(ans)