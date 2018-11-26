import copy
n = int(input())
a = [[0, i] for i in range(n)]

for i in range(n):
    a[i][0] = int(input())
b = sorted(a)
out = copy.deepcopy(b)
out[0][0] = 0
now = 0
for i in range(1, n):
    if b[i - 1][0] == b[i][0]:
        out[i][0] = out[i-1][0]
    else:
        out[i][0] = out[i - 1][0] + 1
for i in range(n):
    # print(out[i])
    a[out[i][1]][0] = out[i][0]
for i in range(n):
    print(a[i][0])