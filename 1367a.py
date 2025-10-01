t = int(input())
for _ in range(t):
    s = list(input())
    s.append(s[-1])
    print("".join(s[i] for i in range(0, len(s), 2)))