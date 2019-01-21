inf = 10**20
def func(n, k, pos):
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
n, k = [int(i) for i in input().split()]
pos = [[0, 0] for _ in range(n)]
for i in range(n):
    pos[i] = [int(i) for i in input().split()]
print(func(n, k, pos))
"""
print("21 vs " + str(func(4, 4, [[1, 4], [3, 3], [6, 2], [8, 1]])))
print("1 vs " + str(func(4, 2, [[0, 0], [1, 1], [2, 2], [3, 3]])))
print("3999999996000000001 vs " + str(func(4, 3, [[-1000000000, -1000000000], [1000000000, 1000000000], [-999999999, 999999999], [999999999, -999999999]])))
# print("print(\"\"+str(func({}, {}, {})))".format(n, k, pos))
"""
