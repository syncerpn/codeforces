t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().strip().split(" ")))
    A = [n + 1 - a for a in A]
    print(" ".join(list(map(str, A))))