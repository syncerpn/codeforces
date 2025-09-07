n = int(input())
A = list(map(int, input().strip().split(" ")))
print("HARD" if any(A) else "EASY")