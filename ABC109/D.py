h, w = [int(i) for i in input().split()]
a = [[0 for j in range(w)] for i in range(h)]
b = [[0 for j in range(w)] for i in range(h)]
for i in range(h):
    a[i] = [int(i) for i in input().split()]

for i in range(h):
    for j in range(w):
        b[i][j] = a[i][j]

counter = 0
for i in range(h):
    for j in range(w-1):
        if (a[i][j] % 2) != 0:
            a[i][j+1] += 1
            a[i][j] -= 1
            counter += 1
for i in range(h-1):
    if (a[i][-1] % 2) != 0:
        a[i+1][-1] += 1
        a[i][-1] -= 1
        counter += 1

print(counter)
for i in range(h):
    for j in range(w-1):
        if b[i][j] % 2 != 0:
            b[i][j+1] += 1
            b[i][j] -= 1
            print("{} {} {} {}".format(i+1, j+1, i+1, j+2))
for i in range(h-1):
    if b[i][-1] % 2 != 0:
        b[i+1][-1] += 1
        b[i][-1] -= 1
        print("{} {} {} {}".format(i+1, w, i+2, w))
