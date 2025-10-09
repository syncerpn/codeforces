from itertools import pairwise
s = "a" + input()
ans = 0
for a, b in pairwise(s):
    d = abs(ord(b) - ord(a))
    ans += min(d, 26 - d)
print(ans)