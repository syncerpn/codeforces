t = int(input())
for _ in range(t):
    n, k = list(map(int, input().strip().split(" ")))
    s = input().strip()
    ans = [0] * n
    v = 1
    p = 0
    for i, c in enumerate(s):
        if i >= k:
            p -= (s[i-k] == "1")
            
        if c == "1":
            ans[i] = v
            v += 1
            p += 1
        
        if i >= k - 1 and p == k:
            print("NO")
            break
    
    else:
        for i in range(n):
            if ans[i] == 0:
                ans[i] = v
                v += 1
        print("YES")
        print(" ".join(list(map(str, ans))))