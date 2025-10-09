t = int(input())
for _ in range(t):
    n = int(input())
    ss = []
    for _ in range(n):
        s = input()
        ss.append(s.index("#") + 1)
    print(" ".join(list(map(str, ss[::-1]))))