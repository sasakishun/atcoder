def func(n, W, w):  # ナップザック問題の亜種
    _max = 0
    weights = [[] for _ in range(4)]
    for i in range(n):
        weights[w[i][0]-w[0][0]].append(w[i][1])
    for i in range(len(weights)):
        weights[i].sort()
        weights[i].append(0)
        weights[i].reverse()
        for j in range(1, len(weights[i])):
            weights[i][j] += weights[i][j-1]
    # print(weights)
    for i in range(len(weights[0])):
        # print("i:{}".format(i))
        for j in range(len(weights[1])):
            # print("j:{}".format(j))
            for k in range(len(weights[2])):
                for l in range(len(weights[3])):
                    # 「i+j+k+l < n」つ選ぶ
                    if w[0][0]*i\
                            + (w[0][0]+1)*j\
                            + (w[0][0]+2)*k\
                            + (w[0][0]+3)*l <= W:
                        # print("i:{} j:{} k:{} l:{} score:{}".format(i, j, k, l, weights[0][i]+weights[1][
                        # j]+weights[2][k]+weights[3][l]))
                        _max = max(_max, weights[0][i]+weights[1][j]+weights[2][k]+weights[3][l])
    return _max


n, W = [int(i) for i in input().split()]
w = [[0, 0] for _ in range(n)]
for i in range(n):
    w[i] = [int(i) for i in input().split()]
print(func(n, W, w))
"""
# print("print(\" vs \" + str(func({}, {}, {})))".format(n, W, w))
print("11 vs " + str(func(4, 6, [[2, 1], [3, 4], [4, 10], [3, 4]])))
print("13 vs " + str(func(4, 6, [[2, 1], [3, 7], [4, 10], [3, 6]])))
print("400 vs " + str(func(4, 10, [[1, 100], [1, 100], [1, 100], [1, 100]])))
print("0 vs " + str(func(4, 1, [[10, 100], [10, 100], [10, 100], [10, 100]])))
"""
