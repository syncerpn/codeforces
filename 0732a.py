k, r = list(map(int, input().strip().split(" ")))
for i in range(1, 10):
    if (k * i % 10 == 0) or (k * i - r) % 10 == 0:
        print(i)
        break
else:
    print(10)