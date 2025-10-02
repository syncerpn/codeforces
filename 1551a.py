t = int(input())
for _ in range(t):
    n = int(input())
    
    m = n // 3
    r = n - m * 3
    if r == 0:
        print(m, m)
    elif r == 1:
        print(m+1, m)
    elif r == 2:
        print(m, m+1)