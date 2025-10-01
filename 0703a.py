n = int(input())
m, c = 0, 0
for _ in range(n):
    a, b = list(map(int, input().strip().split(" ")))
    m += a > b
    c += b > a
print("Mishka" if m > c else ("Chris" if m < c else "Friendship is magic!^^"))