from itertools import pairwise
t = int(input())
for _ in range(t):
    n, k = list(map(int, input().strip().split(" ")))
    A = list(map(int, input().strip().split(" ")))
    if k > 1:
        print("YES")
    else:
        for a, b in pairwise(A):
            if b < a:
                print("NO")
                break
        else:
            print("YES")