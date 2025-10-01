t = int(input())
for _ in range(t):
    a, b, c = list(map(int, input().strip().split(" ")))
    print("STAIR" if a < b < c else ("PEAK" if a < b and b > c else "NONE"))