n, t = list(map(int, input().strip().split(" ")))
s = list(input())
for _ in range(t):
    r = s[:]
    i = 0
    while i < n - 1:
        if s[i] == "B" and s[i+1] == "G":
            r[i] = "G"
            r[i+1] = "B"
            i += 1
        i += 1
    s = r

print("".join(s))