from collections import deque
t = int(input())
for _ in range(t):
    n = int(input())
    g = [[] for _ in range(n+1)]
    d = [0] * (n+1)
    q = deque()
    for _ in range(n-1):
        u, v, x, y = list(map(int, input().strip().split(" ")))
        if x > y:
            g[v].append(u)
            d[u] += 1
        else:
            g[u].append(v)
            d[v] += 1
    
    for u in range(1, n+1):
        if d[u] == 0:
            q.append(u)
    
    ans = [0] * n
    for i in range(1, n+1):
        u = q.popleft()
        ans[u-1] = i
        for v in g[u]:
            d[v] -= 1
            if d[v] == 0:
                q.append(v)
    
    print(" ".join(list(map(str, ans))))