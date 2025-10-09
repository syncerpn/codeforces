t = int(input())
for _ in range(t):
    A = []
    B = []
    for _ in range(4):
        a, b = list(map(int, input().strip().split(" ")))
        A.append(a)
        B.append(b)
    print((max(A) - min(A)) * (max(B) - min(B)))