n = int(input())
s = input()
p = ""
ans = 0
for c in s:
    if c == p:
        ans += 1
    else:
        p = c
print(ans)