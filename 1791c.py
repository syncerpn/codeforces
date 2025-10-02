t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    for i in range((n+1)//2):
        if s[i] == s[~i]:
            print(max(0, n-i*2))
            break
    else:
        print(0)