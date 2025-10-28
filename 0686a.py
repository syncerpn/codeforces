n, x = list(map(int, input().strip().split(" ")))
l = 0
for _ in range(n):
    s, d = list(input().strip().split(" "))
    d = int(d)
    if s == "+":
        x += d
    else:
        if d <= x:
            x -= d
        else:
            l += 1
print(x, l)