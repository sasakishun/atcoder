def func(d, c):
    color = [[0 for _ in range(len(d))] for _ in range(3)]
    for i in range(len(c)):
        for j in range(len(c)):
            color[(i + j) % 3][c[i][j]] += 1
    # print("color:{}".format(color))
    _min = 10**10
    for i in range(len(d)):
        # %3==0を色iにする場合
        cost1 = sum([d[prev][i]*color[0][prev] for prev in range(len(color[0]))])
        for j in range(len(d)):
            if i == j:
                continue
            # %3==1を色jにする場合
            cost2 = sum([d[prev][j] * color[1][prev] for prev in range(len(color[0]))])
            for k in range(len(d)):
                if i == k or j == k:
                    continue
                # %3==2を色kにする場合
                cost3 = sum([d[prev][k] * color[2][prev] for prev in range(len(color[0]))])
                _min = min(_min, cost1+cost2+cost3)
                # print("->{} cost1:{} ->{} cost2:{} ->{} cost3:{} total:{}".format(i, cost1, j, cost2, k, cost3, cost1+cost2+cost3))
    return _min
n, C = [int(i) for i in input().split()]
d = [[0 for _ in range(C)] for _ in range(C)]
c = [[0 for _ in range(n)] for _ in range(n)]
for i in range(C):
    d[i] = [int(i) for i in input().split()]
for i in range(n):
    c[i] = [int(i) - 1 for i in input().split()]
print(func(d, c))
"""
# print("print(func({},{}))".format(d, c))
print(func([[0, 1, 1], [1, 0, 1], [1, 4, 0]],[[0, 1], [2, 2]]))
print(func([[0, 12, 71], [81, 0, 53], [14, 92, 0]],[[0, 0, 1, 0], [1, 0, 0, 1], [1, 1, 0, 2], [0, 0, 1, 1]]))
"""
