t = int(input())
for _ in range(t):
    s = list(input())
    n = len(s)
    ans = []
    for i, c in enumerate(s):
        if c != "0":
            ans.append(c + "0" * (n-1-i))
    print(len(ans))
    print(" ".join(ans))