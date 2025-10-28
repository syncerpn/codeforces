t = int(input())
for _ in range(t):
    s = input()
    if s.count("B") == s.count("A") + s.count("C"):
        print("YES")
    else:
        print("NO")