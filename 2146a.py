from collections import defaultdict
t = int(input())
for _  in range(t):
    n = int(input())
    A = list(map(int, input().strip().split(" ")))
    d = defaultdict(int)
    for a in A:
        d[a] += 1
    d = sorted(list(d.values()))
    k = len(d)
    print(max([(k-i) * a for i, a in enumerate(d)]))