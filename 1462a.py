t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().strip().split(" ")))
    B = [0] * n
    for i in range((n + 1) // 2):
        B[2 * i] = A[i]
    for i in range(n // 2):
        B[2 * i + 1] = A[~i]
    print(" ".join(list(map(str, B))))