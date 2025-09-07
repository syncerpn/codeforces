n = int(input())
ans, c = 0, 0
for _ in range(n):
    a, b = list(map(int, input().strip().split(" ")))
    c = c - a + b
    ans = max(ans, c)
print(ans)