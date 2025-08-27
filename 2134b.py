t = int(input())
for _ in range(t):
    n, k = list(map(int, input().strip().split(" ")))
    A = list(map(int, input().strip().split(" ")))
    for i in range(n):
        m = A[i] % (k+1)
        A[i] += m * k
        
    print(" ".join(list(map(str, A))))