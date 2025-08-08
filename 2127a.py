t = int(input())
for _ in range(t):
    n = int(input())
    d = list(map(int, input().strip().split(" ")))
    s = set(d)
    if 0 in s:
        print("NO")
        continue
    if -1 in s:
        print("YES" if len(s) <= 2 else "NO")
        continue
    print("YES" if len(s) == 1 else "NO")