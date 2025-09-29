n, k = list(map(int, input().strip().split(" ")))
d = 240 - k
for i in range(n):
    c = 5 * i + 5
    if d < c:
        print(i)
        break
    d -= c
else:
    print(n)
        
    