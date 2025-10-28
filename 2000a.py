t = int(input())
for _ in range(t):
    a = input()
    if len(a) < 3:
        print("NO")
    else:
        if a[0:2] != "10":
            print("NO")
        else:
            if a[2] == "0":
                print("NO")
            elif int(a[2:]) == 1:
                print("NO")
            else:
                print("YES")
                