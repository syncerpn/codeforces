P = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
a, b = list(map(int, input().strip().split(" ")))
print("YES" if b in P and P.index(b) - P.index(a) == 1 else "NO")