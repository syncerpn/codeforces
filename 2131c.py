t = int(input())
for _ in range(t):
    n, k = list(map(int, input().strip().split(" ")))
    s = list(map(int, input().strip().split(" ")))
    t = list(map(int, input().strip().split(" ")))
    d = {}
    for a in t:
        p = a % k
        if p > k - p:
            p = k - p
        if p not in d:
            d[p] = 0
        d[p] += 1
    
    for a in s:
        p = a % k
        q = k - p
        if p in d and d[p] > 0:
            d[p] -= 1
        elif q in d and d[q] > 0:
            d[q] -= 1
        else:
            print("NO")
            break
    else:
        print("YES")