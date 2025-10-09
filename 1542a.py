t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().strip().split(" ")))
    print("Yes" if sum(a % 2 for a in A) == n else "No")