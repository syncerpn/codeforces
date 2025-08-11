t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip().split(" ")))
    b = list(map(int, input().strip().split(" ")))
    p, q = 0, 0
    for i in range(n-1, -1, -1):
        if a[i] != b[i] and (a[i] ^ p) != b[i] and (a[i] ^ q) != b[i]:
            print("NO")
            break
        p, q = a[i], b[i]
    else:
        print("YES")