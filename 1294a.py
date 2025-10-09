t = int(input())
for _  in range(t):
    a, b, c, n = list(map(int, input().strip().split(" ")))
    m = a + b + c + n
    print("YES" if m % 3 == 0 and m // 3 >= max(a, b, c) else "NO")