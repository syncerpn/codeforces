# which one to be the last one?
# assume A[i] be the last one to be remained
# then all A[i+1:] must be consumed second
# which accumulate into -sum(A[i+1:])
# max consume of A[0:i] can be calculated with dp
t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().strip().split(" ")))
    s = -sum(A) + A[0]
    m = A[0]
    ans = s
    for i in range(1, n):
        s += A[i]
        ans = max(ans, m + s)
        m = max(m, m - A[i], m + A[i])
    
    print(ans)