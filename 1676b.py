t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().strip().split(" ")))
    m = min(A)
    print(sum(a - m for a in A))