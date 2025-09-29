n = int(input())
m, *A = list(map(int, input().strip().split(" ")))
mi, ma = m, m
ans = 0
for a in A:
    if a > ma:
        ma = a
        ans += 1
    elif a < mi:
        mi = a
        ans += 1
print(ans)