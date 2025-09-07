n, h = list(map(int, input().strip().split(" ")))
A = list(map(int, input().strip().split(" ")))
print(sum(1 if a <= h else 2 for a in A))