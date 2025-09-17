t = int(input())
MOD = 998244353
for _ in range(t):
    n = int(input())
    A = list(map(int, input().strip().split(" ")))
    B = list(map(int, input().strip().split(" ")))
    p, q = 0, 0
    ans = 1
    for a, b in zip(A, B):
        if min(a, b) >= max(p, q):
            ans = (ans * 2) % MOD
        elif min(a, b) < min(p, q):
            print(0)
            break
        p, q = a, b
    else:
        print(ans)