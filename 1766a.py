t = int(input())
for _ in range(t):
    n = int(input())
    s = str(n)
    print(9 * (len(s) - 1) + int(s[0]))