t = int(input())
for _ in range(t):
    a, *A = list(map(int, input().strip().split(" ")))
    print(sum(ai > a for ai in A))