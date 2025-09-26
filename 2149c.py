t = int(input())
for _ in range(t):
    n, k = list(map(int, input().strip().split(" ")))
    A = list(map(int, input().strip().split(" ")))
    s = [True] * k
    ans = k
    j = 0
    for a in A:
        if a < k and s[a]:
            s[a] = False
            ans -= 1
        elif a == k:
            j += 1
    print(max(ans, j))