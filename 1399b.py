t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().strip().split(" ")))
    B = list(map(int, input().strip().split(" ")))
    mA = min(A)
    mB = min(B)
    print(sum(max(a - mA, b - mB) for a, b in zip(A, B)))