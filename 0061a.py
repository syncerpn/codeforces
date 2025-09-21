a = input()
b = input()
print("".join(["1" if ai != bi else "0" for ai, bi in zip(a, b)]))