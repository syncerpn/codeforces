t = int(input())
for _ in range(t):
    n, m, q = list(map(int, input().strip().split(" ")))
    A = sorted(list(map(int, input().strip().split(" "))), reverse=True)
    B = sorted(list(map(int, input().strip().split(" "))), reverse=True)
    Q = []
    for _ in range(q):
        Q.append(list(map(int, input().strip().split(" "))))
    
    