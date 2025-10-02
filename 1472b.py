t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().strip().split(" ")))
    o, t = A.count(1), A.count(2)
    if o % 2 or (o == 0 and t % 2):
        print("NO")
    else:
        print("YES")