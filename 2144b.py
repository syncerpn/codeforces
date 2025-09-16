t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().strip().split(" ")))
    if A.count(0) == 1:
        for i in range(n):
            if A[i] == 0:
                A[i] = n * (n + 1) // 2 - sum(A)
                break
            
    l = 0
    while l < n and A[l] == l + 1:
        l += 1
    
    r = n - 1
    while r >= l and A[r] == r + 1:
        r -= 1
    print(r - l + 1)