inf = float("inf")
t = int(input())
for _ in range(t):
    n, k = list(map(int, input().strip().split(" ")))
    A = []
    for _ in range(n):
        a, b, c = list(map(int, input().strip().split(" ")))
        s = a + b + c
        t = 0
        if a == b and b == c:
            t = inf
        elif a <= b and b <= c:
            t = 2 * min(c - b, c - a, b - a) + 2
        A.append((s, t))
    A.sort()
    
    p, x = A[0]
    if k <= x:
        print(p)
        continue
    
    for i in range(1, n):
        s, t = A[i]
        if k <= x + (s - p) * i:
            print(max(p, p + (k - x) // i))
            break
        k -= x + (s - p) * i
        p, x = s, t
    else:
        print(max(p, p + (k - x) // n))