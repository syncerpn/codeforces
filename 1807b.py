t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().strip().split(" ")))
    print("YES" if sum(a for a in A if a % 2 == 0) - sum(a for a in A if a % 2 == 1) > 0 else "NO")