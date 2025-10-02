from itertools import pairwise
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    s += s[-1]
    v = set()
    for a, b in pairwise(s):
        if b != a:
            if b in v:
                print("NO")
                break
            v.add(a)
    else:
        print("YES")