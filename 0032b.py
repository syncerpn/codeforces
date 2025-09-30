s = input()
n = len(s)
ans = ""
i = 0
while i < n:
    if s[i] == ".":
        ans += "0"
    else:
        if s[i+1] == ".":
            ans += "1"
        else:
            ans += "2"
        i += 1
    i += 1
print(ans)