t = int(input())
for _ in range(t):
    n, w = list(map(int, input().strip().split(" ")))
    r = n % w
    q = n // w
    print(q * (w-1) + r)