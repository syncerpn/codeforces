t = int(input())
for _ in range(t):
    s = input()
    h, m = list(map(int, s.split(":")))
    c = "PM" if h > 11 else "AM"
    print(f"{h%12 if h != 12 and h != 0 else 12:02d}:{m:02d} {c}")