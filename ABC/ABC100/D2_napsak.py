import math

n, m = [int(i) for i in input().split()]
xyz = [[0 for i in range(3)] for j in range(n)]
# y = [0 for i in range(n)]
# z = [0 for i in range(n)]
sum = [[[0 for i in range(3)] for i in range(m + 1)] for j in range(n + 1)]
z_p = [math.inf for i in range(m)]


def search():
    for i in reversed(range(m)):
        for u in range(n):
            if u == 0:
                sum[i][u] = sum[i + 1][u]
            else:
                sum[i][u] = max(abs(sum[i + 1][u][0])
                                + abs(sum[i + 1][u][1])
                                + abs(sum[i + 1][u][2]),
                                abs(sum[i + 1][u - 1][0] + xyz[i][0])
                                + abs(sum[i + 1][u - 1][1] + xyz[i][1])
                                + abs(sum[i + 1][u - 1][2] + xyz[i][2]))
    return sum[0][m]


for i in range(n):
    xyz[i][0], xyz[i][1], xyz[i][2] = [int(i) for i in input().split()]
print(search())
"""
xyz = sorted(xyz)
print(xyz)
plus = 0
minus = 0
for i in range(n - m, n):
    plus += xyz[i][0]
for i in range(m):
    minus += xyz[i][0]
if abs(minus) > abs(plus):
    search(0)
    print(minus)
else:
    search(m)
    print(plus)
"""
