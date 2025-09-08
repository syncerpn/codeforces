t = int(input())
for _ in range(t):
    k, x = list(map(int, input().strip().split(" ")))
    ans = []
    q = 1 << k
    while x != q:
        if x < q:
            ans.append(1)
            x <<= 1
        else:
            ans.append(2)
            x = (x-q) << 1
    
    print(len(ans))
    print(" ".join(list(map(str, ans[::-1]))))