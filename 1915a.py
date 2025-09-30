t = int(input())
for _ in range(t):
    a, b, c = list(map(int, input().strip().split(" ")))
    print(a ^ b ^ c)