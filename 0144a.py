n = int(input())
A = list(map(int, input().strip().split(" ")))
mi, ma = min(A), max(A)
l, r = 0, 0
for i in range(n):
    if A[i] == ma:
        l = i
        break

for i in range(n):
    if A[n-1-i] == mi:
        r = n-1-i
        break

print(l + n - 1 - r - (r < l))