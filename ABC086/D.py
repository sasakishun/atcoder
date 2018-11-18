n, k = [int(i) for i in input().split()]
table = [[0 for i in range(2*k+1)] for j in range(2*k+1)]

for i in range(n):
    x, y, c = input().split()
    x = int(x)
    y = int(y)
    for h in range(len(table)):
        for w in range(len(table)):
            if c == "B":
                if h % (2*k) <= y % (2*k) <= (k - 1 + h) % (2*k)\
                        and w % (2 * k) <= x % (2 * k) <= (k - 1 + w) % (2 * k):
                    table[h][w] += 1
            if c == "W":
                if (h+k) % (2*k) <= y % (2*k) <= (k-1 + h + k) % (2*k)\
                        and (w+k) % (2 * k) <= x % (2 * k) <= (k - 1 + w + k) % (2 * k):
                    table[h][w] += 1
maxCount = 0
for i in range(len(table)):
    for j in range(len(table)):
        maxCount = max(maxCount, table[i][j])
print(maxCount)