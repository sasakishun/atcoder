h, w = [int(i) for i in input().split()]

table = [[0 for j in range(h)] for i in range(w)]
for j in range(h):
    table[0][j] = 1
for i in range(w):
    table[i][0] = 1

for j in range(1, h):
    for i in range(1, w):
        table[i][j] = (table[i - 1][j] + table[i][j - 1]) % (10 ** 9 + 7)
print(table[w - 1][h - 1] % (10 ** 9 + 7))
