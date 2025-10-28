t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().strip().split(" ")))
    A.sort()
    if A[0] == A[-1]:
        print("YES")
    elif n % 2 == 1:
        if A[0] == A[n // 2 - 1] and A[n // 2] == A[-1]:
            print("YES")
        elif A[0] == A[n // 2] and A[n // 2 + 1] == A[-1]:
            print("YES")
        else:
            print("NO")
    else:
        if A[0] == A[n // 2 - 1] and A[n // 2] == A[-1]:
            print("YES")
        else:
            print("NO")