import numpy as np

h, w = [int(i) for i in input().split()]
c = np.full((h, w), 10000)
# c = [[float("inf") for _ in range(w)] for _ in range(h)]
for i in range(h):
    _a = input()
    for j in range(w):
        if _a[j] == "#":
            c[i, j] = 0


for i in range(h):
    for j in range(1, w):
        c[i, j] = min(c[i, j], c[i, j - 1] + 1)


for i in range(1, h):
    for j in range(w):
        c[i, j] = min(c[i, j], c[i - 1, j] + 1)


for i in range(h):
    for j in reversed(range(w - 1)):
        # if c[i][j + 1] != -1:
        c[i, j] = min(c[i, j], c[i, j + 1] + 1)


_max = 0
for i in reversed(range(h - 1)):
    for j in range(w):
        # if c[i+1][j] != -1:
        tmp = min(c[i, j], c[i + 1, j] + 1)
        c[i, j] = tmp
        _max = max(_max, tmp)
print(int(max(_max, c[-1].max())))


