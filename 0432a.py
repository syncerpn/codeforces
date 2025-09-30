n, k = list(map(int, input().strip().split(" ")))
A = list(map(int, input().strip().split(" ")))
A.sort()
ans = 0
for i in range(0, n // 3 * 3, 3):
    if A[i+2] > 5 - k:
        break
    ans += 1
print(ans)