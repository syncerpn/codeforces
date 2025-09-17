from collections import deque
t = int(input())
for _ in range(t):
    n = int(input())
    A = deque(map(int, input().strip().split(" ")))
    for k in range(1, n+1):
        if A[0] == k:
            A.popleft()
        elif A[-1] == k:
            A.pop()
        else:
            print("NO")
            break
    else:
        print("YES")