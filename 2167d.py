t = int(input())
P = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
for _ in range(t):
    n = int(input())
    A = list(map(int, input().strip().split(" ")))
    for p in P:
        for a in A:
            if a % p:
                print(p)
                break
        else:
            continue
        break