n = int(input())
ans = 0
for _ in range(n):
    ans += 1 if "+" in input() else -1

print(ans)
        