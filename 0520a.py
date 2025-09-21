n = int(input())
s = input()
print("YES" if len(set(list(s.lower()))) == 26 else "NO")