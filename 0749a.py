n = int(input())
ans = []
if n % 2:
    ans = [2] * ((n - 3) // 2) + [3]
else:
    ans = [2] * (n // 2)
print(len(ans))
print(" ".join(list(map(str, ans))))