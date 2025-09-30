n = int(input())
A = list(map(int, input().strip().split(" ")))
m = max(A)
print(sum(m - a for a in A))