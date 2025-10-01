t = int(input())
for _ in range(t):
    n = int(input())
    if n % 4 == 0:
        print("YES")
        e = [2*i for i in range(1, n//2+1)]
        o = [2*i+1 for i in range(n//2 - 1)]
        o.append(sum(e) - sum(o))
        e += o
        print(" ".join(list(map(str, e))))
    else:
        print("NO")