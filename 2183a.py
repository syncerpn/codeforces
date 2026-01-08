t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().strip().split(" ")))
    print("Bob" if A[0] == A[-1] == 0 else "Alice")