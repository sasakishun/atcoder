inf = 10 ** 20


def func(n, _k, pos):
    x = [pos[i][0] for i in range(len(pos))]
    y = [pos[i][1] for i in range(len(pos))]
    x.sort()
    y.sort()
    imos = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if pos[i][0] == x[j] and pos[i][1] == y[k]:
                    imos[j][k] += 1
    for i in range(n):
        for j in range(1, n):
            imos[i][j] += imos[i][j - 1]
    for i in range(1, n):
        for j in range(n):
            imos[i][j] += imos[i - 1][j]
    # for i in reversed(range(len(imos))):
        # print(imos[i])

    def getImos(_right, _left, _upper, _bottom):
        _sum = imos[_right][_upper]
        if _bottom > 0:
            _sum -= imos[_right][_bottom - 1]
        if _left > 0:
            _sum -= imos[_left - 1][_upper]
        if _bottom > 0 and _left > 0:
            _sum += imos[_left - 1][_bottom - 1]
        return _sum

    _min = inf
    for left in range(len(x) - 1):
        for right in range(left + 1, len(x)):
            for bottom in range(len(y) - 1):
                for upper in range(bottom + 1, len(y)):
                    """
                    print("{} {} {} {} :{}poi s:{}".format(right, left, bottom, upper,
                                                        getImos(right, left, upper, bottom),
                                                        (x[right] - x[left]) * (y[upper] - y[bottom])))
                    """
                    if getImos(right, left, upper, bottom) >= _k:
                        _min = min(_min, (x[right] - x[left]) * (y[upper] - y[bottom]))
                        # print("s:{}".format((x[right] - x[left]) * (y[upper] - y[bottom])))
    return _min
    """
    out = inf
    for i in range(n):
        # pos[i]を含む長方形を考える
        box = [[pos[i][0], pos[i][1]] for _ in range(4)]
        used = [False for _ in range(n)]
        used[i] = True
        minS = 0
        for _k in range(k-1):
            minS = inf
            using = -1
            for j in range(n):
                if not used[j]:
                    s = (max(box[1][0], pos[j][0]) - min(box[0][0], pos[j][0])) \
                        * (max(box[1][1], pos[j][1]) - min(box[2][1], pos[j][1]))
                    if s < minS:
                        minS = s
                        using = j
            used[using] = True
            right = max(box[1][0], pos[using][0])
            left = min(box[0][0], pos[using][0])
            upper = max(box[1][1], pos[using][1])
            botom = min(box[2][1], pos[using][1])
            box = [[left, upper], [right, upper], [right, botom], [left, botom]]
            # print("i:{} _k:{} minS:{} box:{}".format(i, _k, minS, box))
        # if minS != math.inf:
            # print(minS)
        out = min(out, minS)
    return out
    """


n, k = [int(i) for i in input().split()]
pos = [[0, 0] for _ in range(n)]
for i in range(n):
    pos[i] = [int(i) for i in input().split()]
print(func(n, k, pos))
"""
print("21 vs " + str(func(4, 4, [[1, 4], [3, 3], [6, 2], [8, 1]])))
print("1 vs " + str(func(4, 2, [[0, 0], [1, 1], [2, 2], [3, 3]])))
print("3999999996000000001 vs " + str(func(4, 3, [[-1000000000, -1000000000], [1000000000, 1000000000],
                                                  [-999999999, 999999999], [999999999, -999999999]])))
"""
# print("print(\"\"+str(func({}, {}, {})))".format(n, k, pos))
