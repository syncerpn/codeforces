t = int(input())
for _  in range(t):
    A = list(map(int, input().strip().split(" ")))
    A.sort()
    print("YES" if A[0] + A[1] == A[2] else "NO")