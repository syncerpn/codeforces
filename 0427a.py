n = int(input())
A = list(map(int, input().strip().split(" ")))
p = 0
ans = 0
for a in A:
    p += a
    if p < 0:
        p = 0
        ans += 1

print(ans)