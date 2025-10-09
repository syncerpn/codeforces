t = int(input())
for _ in range(t):
    n = int(input())
    a = input()
    b = input()
    for ai, bi in zip(a, b):
        if (ai == "R" and bi != ai) or (bi == "R" and ai != bi):
            print("NO")
            break
    else:
        print("YES")