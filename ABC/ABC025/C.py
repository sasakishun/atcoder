"""
b = [[0 for _ in range(3)] for _ in range(2)]
c = [[0 for _ in range(2)] for _ in range(3)]

for i in range(2):
    b[i] = [int(i) for i in input().split()]
for i in range(3):
    c[i] = [int(i) for i in input().split()]
"""
b = [[0,15,0],[0,0,25]]
c = [[20,0],[0,0],[25,0]]
_max = 0
N = [i for i in range(9)]  # N = bit探索する桁数
# Nの要素の全組み合わせが出力
for i in range(1, 1 << len(N)):
    output = []
    selected = [0 for _ in range(9)]
    for j in range(len(N)):
        if ((i >> j) & 1) == 1:
            output.append(j)  # このjが今回探索するindexの1つ
            selected[j] = 1
    if len(output) == 5:
        # スコアを算出
        score = 0
        naoko = 0
        for _i in range(2):
            for _j in range(3):
                # print("i:{} j:{}".format(_i, _j))
                # print("s1:{} s2:{}".format(_i * 3 + _j, (_i+1) * 3 + _j))
                if selected[_i * 3 + _j] == 1\
                        and selected[(_i+1) * 3 + _j] == 1:
                    score += b[_i][_j]
                else:
                    naoko += b[_i][_j]
        for _i in range(3):
            for _j in range(2):
                if selected[_i + 3 * _j] == 1\
                        and selected[_i + 1 + 3 * _j] == 1:
                    score += c[_i][_j]
                else:
                    naoko += c[_i][_j]
        print("score:{} vs {}".format(score, naoko))
        # print(output)