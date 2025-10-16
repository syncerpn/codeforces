t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().strip().split(" ")))
    ans = []
    for a in A:
        if ans and a < ans[-1]:
            ans.append(a)
        ans.append(a)
    print(len(ans))
    print(" ".join(list(map(str, ans))))