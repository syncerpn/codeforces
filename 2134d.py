t = int(input())
for _ in range(t):
    n = int(input())
    g = [[] for _ in range(n + 1)]
    m = 0
    k = 0
    for _ in range(n):
        a, b = list(map(int, input().strip().split(" ")))
        g[a].append(b)
        g[b].append(a)
        
        if len(g[a]) > m:
            m = len(g[a])
            k = a
            
        if len(g[b]) > m:
            m = len(g[b])
            k = b
        
        