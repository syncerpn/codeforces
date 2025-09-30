n = int(input())
A = list(map(int, input().strip().split(" ")))
l, r = 0, n-1
ans = [0, 0]
for i in range(n):
    if A[r] > A[l]:
        ans[i%2] += A[r]
        r -= 1
    else:
        ans[i%2] += A[l]
        l += 1
print(ans[0], ans[1])
        
