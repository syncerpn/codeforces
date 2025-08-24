n = int(input())
ans = 0
for _ in range(n):
    ans += sum(list(map(int, input().strip().split(" ")))) >= 2

print(ans)
        