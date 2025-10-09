t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print(max(ord(c) - 96 for c in s))