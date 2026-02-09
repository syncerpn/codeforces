t = int(input())
for _ in range(t):
    n, k, x = list(map(int, input().strip().split(" ")))
    if k == 1:
        print("NO")
    elif x != 1:
        print("YES")
        print(n)
        print(" ".join(["1"] * n))
    elif k == 2:
        if n % 2 == 1:
            print("NO")
        else:
            print("YES")
            print(n // 2)
            print(" ".join(["2"] * (n // 2)))
    else:
        print("YES")
        if n % 2 == 1:
            print(1 + (n - 3) // 2)
            print(" ".join(list(map(str, [3] + [2] * ((n - 3) // 2)))))
        else:
            print(n // 2)
            print(" ".join(["2"] * (n // 2)))