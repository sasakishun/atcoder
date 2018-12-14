a, b = [int(i) for i in input().split()]

counter = 0
for i in range(1, 1000):
    if i == b - a:
        print(counter-a)
        exit()
    counter += i
