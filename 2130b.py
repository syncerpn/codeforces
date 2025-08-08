import collections
t = int(input())
for _ in range(t):
    n, s = list(map(int, input().strip().split(" ")))
    d = list(map(int, input().strip().split(" ")))
    p = collections.Counter(d)
    ans = p[1] + 2 * p[2]
    q = s - ans
    if q == 0:
        print(-1)
    elif q < 0:
        print(" ".join(list(map(str, d))))
    else:
        if q % 2 == 0 or q > 1:
            print(-1)
        else:
            d = [0] * p[0] + [2] * p[2] + [1] * p[1]
            print(" ".join(list(map(str, d))))