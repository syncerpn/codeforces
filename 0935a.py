n = int(input())
s = int(n ** 0.5) + 1
ans = 0
for i in range(1, s):
    if n % i == 0:
        p = n // i
        ans += (p > 1) + (i > 1)
        if p == i:
            ans -= 1
print(ans)