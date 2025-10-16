from collections import Counter
t = int(input())
for _ in range(t):
    n, m = list(map(int, input().strip().split(" ")))
    s = input()
    d = Counter(s)
    ans = 0
    for k in "ABCDEFG":
       ans += max(0, m - d[k])
    print(ans)