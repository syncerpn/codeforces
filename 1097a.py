r = input()
S = list(input().strip().split(" "))
for s in S:
    if s[0] == r[0] or s[1] == r[1]:
        print("YES")
        break
else:
    print("NO")