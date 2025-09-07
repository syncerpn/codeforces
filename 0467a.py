n = int(input())
ans = 0
for _ in range(n):
    p, q = list(map(int, input().strip().split(" ")))
    ans += q - p >= 2
print(ans)