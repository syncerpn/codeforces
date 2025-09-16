from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().strip().split(" ")))
    if sum(A) % 3 != 0:
        print(0, 0)
    else:
        b = 0
        d = defaultdict(list)
        for i, a in enumerate(A):
            b = (b + a) % 3
            d[b].append(i+1)
            if len(d[b]) == 2 and d[b][1] < n:
                print(d[b][0], d[b][1])
                break
        else:
            print(1, 2)