t = int(input())
for _ in range(t):
    for _ in range(3):
        s = input()
        if "?" in s:
            if "B" in s:
                if "C" in s:
                    print("A")
                else:
                    print("C")
            else:
                print("B")
                
        