import math

n, m = [int(i) for i in input().split()]
xyz = [[0 for i in range(3)] for j in range(n)]
# y = [0 for i in range(n)]
# z = [0 for i in range(n)]

sum = [[math.inf for i in range(n)] for j in range(n)]

z_p = [math.inf for i in range(m)]

for i in range(n):
    xyz[i][0], xyz[i][1], xyz[i][2] = [int(i) for i in input().split()]
xyz = sorted(xyz)
print(xyz)
plus = 0
minus = 0
for i in range(n - m, n):
    plus += xyz[i][0]
for i in range(m):
    minus += xyz[i][0]
if abs(minus) > abs(plus):
    print(minus)
else:
    print(plus)
