n = int(input())
A = list(map(int, input().strip().split(" ")))
ss = [[], [], []]
for i, a in enumerate(A):    
    ss[a-1].append(i+1)

m = min(len(ss[i]) for i in range(3))
print(m)
if m > 0:
    for i in range(m):
        print(ss[0][i], ss[1][i], ss[2][i])
