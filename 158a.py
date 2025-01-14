n, k = list(map(int, input().split(" ")))

aa = list(map(int, input().split(" ")))
t = max(aa[k-1], 1)
print(sum([a >= t for a in aa]))
        