w, h, n = [int(i) for i in input().split()]
table = [[0 for _ in range(w)] for _ in range(h)]

for _ in range(n):
    x, y, a = [int(i) for i in input().split()]
    if a == 1:
        table[0][0] += 1
        if x < w:
            table[0][x] -= 1
    elif a == 2:
        if x < w:
            table[0][x] += 1
    elif a == 3:
        table[0][0] += 1
        if y < h:
            table[y][0] -= 1
    elif a == 4:
        if y < h:
            table[y][0] += 1

for i in range(len(table)):
    for j in range(1, len(table[i])):
        table[i][j] += table[i][j-1]
for i in range(1, len(table)):
    for j in range(len(table[i])):
        table[i][j] += table[i-1][j]
count = 0
for i in range(len(table)):
    for j in range(len(table[i])):
        if table[i][j] == 0:
            count += 1
print(count)
