n, m = [int(i) for i in input().split()]
a = [[0, 0] for _ in range(n)]
c = [[0, 0] for _ in range(m)]
for i in range(n):
    a[i] = [int(i) for i in input().split()]
for i in range(m):
    c[i] = [int(i) for i in input().split()]

for i in range(n):
    _min = [10 ** 10, 0]
    for j in range(m):
        if abs(a[i][0] - c[j][0]) + abs(a[i][1] - c[j][1]) < _min[0]:
            _min[0] = abs(a[i][0] - c[j][0]) + abs(a[i][1] - c[j][1])
            _min[1] = j + 1
    print(_min[1])
