t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().strip().split(" ")))
    if A[0] != A[1]:
        if A[1] == A[2]:
            print(1)
        else:
            print(2)
    else:
        for i in range(2, n):
            if A[i] != A[0]:
                print(i+1)
                break