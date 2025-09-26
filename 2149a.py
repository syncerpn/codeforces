t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().strip().split(" ")))
    print((A.count(-1) % 2) * 2 + A.count(0))