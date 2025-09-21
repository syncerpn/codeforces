from collections import Counter
a = input() + input()
b = input()
print("YES" if Counter(a) == Counter(b) else "NO")