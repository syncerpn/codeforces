t = int(input())
for _ in range(t):
    A = list(map(int, input().strip().split(" ")))
    print(max(A) - min(A))