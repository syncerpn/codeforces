t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().strip().split(" ")))
    A = [a % 2 for a in A]
    if sum(A) == 0 or (sum(A) == n and n % 2 == 0):
        print("NO")
    else:
        print("YES")