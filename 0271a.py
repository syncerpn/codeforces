n = int(input())
k = n + 1
s = list(str(k))
while len(s) != len(set(s)):
    k += 1
    s = list(str(k))
print(k)