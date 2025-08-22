DP = []
for i in range(19):
    if i == 0:
        DP.append(3)
    else:
        DP.append((i+9)*(3**i)//3)
        
t = int(input())
for _ in range(t):
    n, k = list(map(int, input().strip().split(" ")))
    min_deal = 0
    i, j = 0, 1
    
    nn = n
    d = []
    while nn > 0:
        m = nn % 3
        d.append(m)
        nn //= 3
        i += 1
        j *= 3
    
    if k < sum(d):
        print(-1)
        continue
    
    while sum(d) < k and len(d) > 1:
        if d[-1] * 2 + sum(d) <= k:
            d[-2] += d[-1] * 3
            d.pop()
        else:
            dd = (k - sum(d)) // 2
            d[-2] += dd * 3
            d[-1] -= dd
            break
    print(sum(d[i] * DP[i] for i in range(len(d))))