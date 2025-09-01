s = input()
n = str(s.count("4") + s.count("7"))
t = set(list(n))
if "4" in t:
    t.remove("4")
if "7" in t:
    t.remove("7")
print("NO" if len(t) > 0 else "YES")