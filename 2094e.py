# we need to test every a_k
# the point is how can we do it fast?
# turn out, we can check the set bit of every element
# if we choose a_k and i-th bit of a_k is set
# we can add 2 ** i * count of non-set bit of others
# or if i-th bit of a_k is not set
# we can add 2 ** i * count of set bit of others
t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().strip().split(" ")))
    ans = 0
    d = [0] * 30
    ans = [0] * n
    for a in A:
        for i in range(30):
            m = (a >> i) & 1
            d[i] += m
            
    for j, a in enumerate(A):
        for i in range(30):
            m = (a >> i) & 1
            if not m:
                ans[j] += d[i] * 2 ** i
            else:
                ans[j] += (n - d[i]) * 2 ** i
    print(max(ans))