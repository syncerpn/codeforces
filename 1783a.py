from collections import deque
t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().strip().split(" ")))
    if min(A) == max(A):
        print("NO")
    else:
        A.sort(reverse=True)
        A = deque(A)
        while A[0] == A[1]:
            A.append(A.popleft())
        print("YES")
        print(" ".join(list(map(str, A))))