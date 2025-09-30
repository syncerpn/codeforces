t = int(input())
for _ in range(t):
    A = list(map(int, input().strip().split(" ")))
    A.sort()
    print(A[1])