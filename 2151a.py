from itertools import pairwise
t = int(input())
for _  in range(t):
    n, m = list(map(int, input().strip().split(" ")))
    B = list(map(int, input().strip().split(" ")))
    for a, b in pairwise(B):
        if b <= a:
            print(1)
            break
    else:
        print(n - B[-1] + 1)