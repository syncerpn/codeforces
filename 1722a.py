t = int(input())
r = tuple(sorted("Timur"))
for _ in range(t):
    n = int(input())
    s = input()
    print("YES" if tuple(sorted(s)) == r else "NO")