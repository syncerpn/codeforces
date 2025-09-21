klmn = [int(input()), int(input()), int(input()), int(input())]
d = int(input())
ans = 0
for a in range(1, d+1):
    for b in klmn:
        if a % b == 0:
            ans += 1
            break
print(ans)