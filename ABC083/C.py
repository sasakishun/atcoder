x, y = [int(i) for i in input().split()]

i = 1
while True:
    x *= 2
    if x > y:
        print(i)
        exit()
    i += 1