t = int(input())
d = {"p": "q", "q": "p", "w": "w"}
for _ in range(t):
    s = input()
    r = ""
    for i in range(len(s)):
        r += d[s[~i]]
    print(r)