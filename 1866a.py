n = int(input())
A = list(map(int, input().strip().split(" ")))
print(min([abs(a) for a in A]))