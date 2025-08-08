t = int(input())
for _ in range(t):
    n, x = list(map(int, input().strip().split(" ")))
    x -= 1
    s = input().strip()
    l, r = -1, -1
    for i in range(x-1, -1, -1):
        if s[i] == "#":
            l = i
            break
    for i in range(x+1, n):
        if s[i] == "#":
            r = i
            break
    
    if l == -1 and r == -1:
        print(1)
    elif l == -1:
        print(min(x+1, n-r+1))
    elif r == -1:
        print(min(l+2, n-x))
    else:
        print(max(min(x+1, n-r+1), min(l+2, n-x)))
        