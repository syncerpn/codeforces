n = int(input())
p = ""
ans = 0
for _ in range(n):
    a = input()
    if a != p:
        ans += 1
    p = a
print(ans)