t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    m = []
    ans = []
    for i, c in enumerate(s):
        if c == "1":
            m.append(i+1)
        elif c == "2":
            if m:
                m.pop()
                ans.append(i+1)
    ans += m
    ans.sort()
    print(len(ans))
    print(" ".join(list(map(str, ans))))