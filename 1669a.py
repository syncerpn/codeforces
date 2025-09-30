t = int(input())
for _ in range(t):
    r = int(input())
    d = 4
    if r >= 1900:
        d = 1
    elif r >= 1600:
        d = 2
    elif r >= 1400:
        d = 3
    print(f"Division {d}")