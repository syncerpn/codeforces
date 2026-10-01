t = int(input())
for _ in range(t):
    n, m = list(map(int, input().strip().split(" ")))
    A = set(list(map(int, input().strip().split(" "))))
    B = set(list(map(int, input().strip().split(" "))))
    print(len(A.intersection(B)))