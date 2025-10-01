A = list(map(int, input().strip().split(" ")))
s = input()
print(sum(A[int(c) - 1] for c in s))
