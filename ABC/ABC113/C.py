n, m = [int(i) for i in input().split()]
p = [0 for i in range(m)]
y = [0 for i in range(m)]

out = [[0, 0] for i in range(m)]
hash = [[] for i in range(10**5+1)]
for i in range(m):
    p[i], y[i] = [int(i) for i in input().split()]
    hash[p[i]].append([y[i], i])

for i in range(len(hash)):
    hash[i] = sorted(hash[i])
    for j in range(len(hash[i])):
        out[hash[i][j][1]] = i, j+1
for i in range(len(out)):
    print("{}{}".format(str(out[i][0]).zfill(6), str(out[i][1]).zfill(6)))