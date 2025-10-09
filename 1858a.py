t = int(input())
for _ in range(t):
    a, b, c = list(map(int, input().strip().split(" ")))
    print("First" if a + c - c // 2 > b + c // 2 else "Second")