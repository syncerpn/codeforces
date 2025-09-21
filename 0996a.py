n = int(input())
ans = 0
for a in [100, 20, 10, 5, 1]:
    ans += n // a
    n -= n // a * a
print(ans)