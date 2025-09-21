n, m = list(map(int, input().strip().split(" ")))
ans = ["#" * m if i % 2 == 0 else ("." * (m-1) + "#" if i % 4 == 1 else "#" + "." * (m-1)) for i in range(n)]
print("\n".join(ans))