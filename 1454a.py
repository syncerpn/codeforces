t = int(input())
for _ in range(t):
    n = int(input())
    print(" ".join(list(map(str, [n] + list(range(1, n))))))