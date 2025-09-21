n = int(input())
A = list(map(int, input().strip().split(" ")))
B = list(map(int, input().strip().split(" ")))
print("I become the guy." if len(set(A[1:] + B[1:])) == n else "Oh, my keyboard!")