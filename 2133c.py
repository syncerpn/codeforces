import sys

t = int(input())
for _ in range(t):
    layers = {}
    n = int(input())
    big = -1
    path = []
    for i in range(n):
        print(f"? {i + 1} {n} {' '.join(list(map(str, list(range(1, n + 1)))))}")
        sys.stdout.flush()
        ans = int(input())
        if ans in layers:
            layers[ans].append(i + 1)
        else:
            layers[ans] = [i + 1]
        if ans > big:
            big = ans
            path = [i + 1]
    for depth in range(big - 1, 0, -1):
        for candidate in layers[depth]:
            print(f"? {path[-1]} 2 {path[-1]} {candidate}")
            sys.stdout.flush()
            ans = int(input())
            if ans == 2:
                path.append(candidate)
                break
    print(f"! {len(path)} {' '.join(list(map(str, path)))}")
    sys.stdout.flush()