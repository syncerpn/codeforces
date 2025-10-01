t = int(input())
r = "codeforces"
for _ in range(t):
    s = input()
    print(sum(a != b for a, b in zip(s, r)))