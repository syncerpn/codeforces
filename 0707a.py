n, m = list(map(int, input().strip().split(" ")))
for _ in range(n):
    s = input()
    if "Y" in s or "C" in s or "M" in s:
        print("#Color")
        break
else:
    print("#Black&White")