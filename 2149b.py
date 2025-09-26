t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().strip().split(" ")))
    A.sort()
    print(max(abs(A[i]-A[i+1]) for i in range(0,n,2)))