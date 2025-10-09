t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    x, y = 0, 0
    for c in s:
        if c == "L":
            x -= 1
        elif c == "R":
            x += 1
        elif c == "U":
            y += 1
        else:
            y -= 1
        if x == 1 and y == 1:
            print("YES")
            break
    else:
        print("NO")