def func(n, m, x, y, z):
    _max = -10**10
    for i in range(2):
        for j in range(2):
            for k in range(2):
                sign = ["+", "+", "+"]
                if i == 1:
                    sign[0] = "-"
                if j == 1:
                    sign[1] = "-"
                if k == 1:
                    sign[2] = "-"
                xyz = [eval("{}{}{}{}{}{}".format(sign[0], x[l],
                                      sign[1], y[l],
                                      sign[2], z[l])) for l in range(n)]
                xyz.sort()
                # print(xyz)
                _sum = sum(xyz[n-m:])
                _max = max(_max, _sum)
    return _max

n, m = [int(i) for i in input().split()]
x = [0 for _ in range(n)]
y = [0 for _ in range(n)]
z = [0 for _ in range(n)]
for i in range(n):
    x[i], y[i], z[i] = [int(i) for i in input().split()]
print(func(n, m, x, y, z))
"""
print("print(func({}, {}, {}, {}, {}))".format(n, m, x, y, z))
print(56 == func(5, 3, [3, 1, 2, 3, 9], [1, 5, 6, 5, 7], [4, 9, 5, 8, 9]))
print(54 == func(5, 3, [1, -4, 7, -10, 13], [-2, 5, -8, 11, -14], [3, -6, -9, -12, 15]))
print(638 == func(10, 5, [10, 23, -94, -26, -69, -26, -72, 21, 40, -62], [-80, 8, 28, -2, 72, -86, -50, 65, -94, 18],
           [21, 38, 11, 18, 79, -54, 59, -32, 87, 82]))
"""
