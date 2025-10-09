t = int(input())
for _ in range(t):
    n, k = list(map(int, input().strip().split(" ")))
    A = list(map(int, input().strip().split(" ")))
    B = list(map(int, input().strip().split(" ")))
    if k == 0:
        print(sum(A))
    else:
        B.sort()
        C = A + B[-k:]
        C.sort()
        print(sum(C[-n:]))