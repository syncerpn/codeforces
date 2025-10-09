t = int(input())
for _ in range(t):
    ss = []
    for _ in range(8):
        s = input()
        ss.append(s)
    ss = sum(list(map(list, zip(*ss))), start=[])
    
    print("".join(ss).strip("."))