t = int(input())
for _ in range(t):
    n = int(input())
    P = list(map(int, input().strip().split(" ")))
    Q = []
    for a in P:
        Q.append(n+1-a)
    print(" ".join(list(map(str, Q))))