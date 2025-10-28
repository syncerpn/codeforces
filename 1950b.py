t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(2 * n):
        for j in range(2 * n):
            d = (i // 2 % 2) ^ (j // 2 % 2)
            if d:
                print(".", end="")
            else:
                print("#", end="")
        print()