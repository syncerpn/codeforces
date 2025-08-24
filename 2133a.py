t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, input().strip().split(" ")))
    if len(s) != len(set(s)):
        print("YES")
    else:
        print("NO")