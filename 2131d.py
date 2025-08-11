# good problem
# for a given root r, the number of operations needed to make all other nodes connected to r
# equal the number of leaves not directly connected to r at the beginning
# the reason is that, we have to visit all those leaves from r
# so just need to count the number of leaves at first
# and check number of leaves not directly connect to every node as the root
t = int(input())
for _ in range(t):
    n = int(input())
    d = {}
    s = {}
    for _ in range(n-1):
        u, v = list(map(int, input().strip().split(" ")))
        if u not in d:
            d[u] = 0
            s[u] = []
        d[u] += 1
        s[u].append(v)
        if v not in d:
            d[v] = 0
            s[v] = []
        d[v] += 1
        s[v].append(u)
    l = set()
    for u in d:
        if d[u] == 1:
            l.add(u)
    m = len(l)
    ans = n
    for u in s:
        k = 0
        if u in l:
            k += 1
        for v in s[u]:
            if v in l:
                k += 1
        ans = min(ans, m - k)
    print(ans)