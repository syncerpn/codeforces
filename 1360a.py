t = int(input())
for _ in range(t):
    a, b = list(map(int, input().strip().split(" ")))
    print(max(2 * min(a, b),  max(a, b)) ** 2)