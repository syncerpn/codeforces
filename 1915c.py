t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().strip().split(" ")))
    s = int(sum(A) ** 0.5)
    if s * s == sum(A):
        print("YES")
    else:
        print("NO")
    