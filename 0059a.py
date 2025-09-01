s = input()
L = "abcdefghijklmnopqrstuvwxyz"
l = 0
for c in s:
    if c in L:
        l += 1

u = len(s) - l
print(s.upper() if u > l else s.lower())