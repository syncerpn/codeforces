n = int(input())
ans = 0
A = []
for _ in range(n):
    h, a = list(map(int, input().strip().split(" ")))
    for k, b in A:
        ans += (h == b) + (a == k)
    A.append((h, a))
print(ans)