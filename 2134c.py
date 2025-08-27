t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().strip().split(" ")))
    if len(A) % 2 == 0:
        A.append(0)
    ans = 0
    for i in range(1, n, 2):
        if A[i-1] > A[i]:
            ans += A[i-1] - A[i]
            A[i-1] = A[i]
        
        if A[i+1] > A[i]:
            ans += A[i+1] - A[i]
            A[i+1] = A[i]
            
        if A[i-1] + A[i+1] > A[i]:
            b = min(A[i+1], A[i-1] + A[i+1] - A[i])
            ans += b
            A[i+1] -= b
            
        if A[i-1] + A[i+1] > A[i]:
            b = A[i-1] + A[i+1] - A[i]
            ans += b
            A[i-1] -= b
    print(ans)