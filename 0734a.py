n = int(input())
s = input()
a = s.count("A")
d = len(s) - a
print("Friendship" if a == d else ("Anton" if a > d else "Danik"))