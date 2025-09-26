t = int(input())
for _ in range(t):
    n, k, l, r = list(map(int, input().strip().split(" ")))
    A = list(map(int, input().strip().split(" ")))
    b = 0
    d = {}
    ans = 0
    for c in range(n):
        ac = A[c]
        if ac not in d:
            d[ac] = 0
        d[ac] += 1
        while len(d) > k or c - b + 1 > r:
            ab = A[b]
            d[ab] -= 1
            if d[ab] == 0:
                del d[ab]
            b += 1
            
        if len(d) == k and l <= c - b + 1 <= r:
            ans += 1
    
    print(ans)