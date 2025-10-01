a, b = list(map(int, input().strip().split(" ")))
p = 7 - max(a, b)
if p == 1:
    print("1/6")
elif p == 2:
    print("1/3")
elif p == 3:
    print("1/2")
elif p == 4:
    print("2/3")
elif p == 5:
    print("5/6")
elif p == 6:
    print("1/1")
elif p == 0:
    print("0/1")
    
    