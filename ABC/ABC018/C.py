"""
r, c, k = [4, 5, 2]
# 縦"k"横"k"のひし形で塗る
s = [['x', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'x'], ['o', 'o', 'o', 'o', 'o'], ['o', 'x', 'x', 'o', 'o']]
"""
r, c, k = [int(i) for i in input().split()]
s = [["0" for _ in range(c)] for _ in range(r)]
for i in range(len(s)):
    s[i][0:c] = input()
table = [[[0, 0, 0, 0] for _ in range(c)] for _ in range(r)]
# table[i][j]->[a, b]の場合、[i][j]の上にaつ連続した"o"があり
# 下にbつ連続した"o"がある

# 全てのi,j->O(500*500) x,y->O(500*500)
for j in range(c):
    count = 0
    for i in range(r):
        if s[i][j] == "o":
            count += 1
        else:
            count = 0
        table[i][j][0] = count
    count = 0
    for i in reversed(range(r)):
        if s[i][j] == "o":
            count += 1
        else:
            count = 0
        table[i][j][1] = count
for i in range(r):
    count = 0
    for j in range(c):
        if s[i][j] == "o":
            count += 1
        else:
            count = 0
        table[i][j][2] = count
    count = 0
    for j in reversed(range(c)):
        if s[i][j] == "o":
            count += 1
        else:
            count = 0
        table[i][j][3] = count
out = 0
# for i in table:
# print(i)
for i in range(k - 1, len(table) - k + 1):
    for j in range(len(table[0]) - 2 * k + 2):
        # print()
        okFlag = True
        for _k in range(j, j + k):
            # print("1,i:{} j:{} _k:{} {} height:{}".format(i, j, _k, okFlag, _k - j))
            if min(table[i][_k][0], table[i][_k][1]) <= _k - j:
                okFlag = False
        for _k in range(j + k, j + 2 * k - 1):
            # print("2,i:{} j:{} _k:{} {} height:{}".format(i, j, _k, okFlag, k - (_k - j)))
            if min(table[i][_k][0], table[i][_k][1]) <= k - (_k - j):
                okFlag = False
        if okFlag:
            out += 1
            # print("i:{} j:{} {}".format(i, j, okFlag))
print(out)
