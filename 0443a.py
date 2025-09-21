s = input()[1:-1]
if s:
    print(len(set(s.split(", "))))
else:
    print(0)