t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().strip().split(" ")))
    A.sort()
    A[0] += 1
    ans = 1
    for a in A:
        ans *= a
    print(ans)