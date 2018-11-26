n = int(input())
a = [int(i) for i in input().split()]
table = [[[-10000, -10000] for i in range(n)] for j in range(n)]

maxScore = -10000
# 全探索
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        takahashi = 0
        aoki = 0
        for k in range(min(i, j), max(i, j)+1):
            if (min(i, j)+k) % 2 != 0:
                aoki += a[k]
            else:
                takahashi += a[k]
        table[i][j] = [takahashi, aoki]
for i in range(n):
    # print(table[i])
    aokiMax = table[i][0][1]
    aokiMaxIndex = 0
    for j in range(1, n):
        if table[i][j][1] > aokiMax:
            aokiMax = table[i][j][1]
            aokiMaxIndex = j
    maxScore = max(maxScore, table[i][aokiMaxIndex][0])
print(maxScore)
# for i in range(n):
    # print(table[i])