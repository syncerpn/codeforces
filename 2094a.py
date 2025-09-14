t = int(input())
for _ in range(t):
    s = input()
    ans = [c[0] for c in s.split(" ")]
    print("".join(ans))
