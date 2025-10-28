t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().strip().split(" ")))
    B = sorted(A)
    D = [a - B[-1] if a != B[-1] else a - B[-2] for a in A]
    print(" ".join(list(map(str, D))))