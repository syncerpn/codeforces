t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().strip().split(" ")))
    f = sum(a % 2 for a in A)
    if f == 0 or f == n:
        print(" ".join(list(map(str, A))))
    else:
        print(" ".join(list(map(str, sorted(A)))))