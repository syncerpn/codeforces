t = int(input())
for _ in range(t):
    x, y, z = list(map(int, input().strip().split(" ")))
    if x == y and z <= x:
        print("YES")
        print(x, z, z)
    elif y == z and x <= y:
        print("YES")
        print(x, x, y)
    elif z == x and y <= z:
        print("YES")
        print(y, x, y)
    else:
        print("NO")