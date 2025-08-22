t = int(input())
for _ in range(t):
    n = int(input())
    a = input()
    m = int(input())
    b = input()
    c = input()
    for i, ci in enumerate(c):
        if ci == "D":
            a = a + b[i]
        else:
            a = b[i] + a
    print(a)