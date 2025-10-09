t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    for l in range(n):
        if s[l] == "B":
            break
    else:
        print(0)
        continue
    for r in range(n-1, l-1, -1):
        if s[r] == "B":
            print(r - l + 1)
            break