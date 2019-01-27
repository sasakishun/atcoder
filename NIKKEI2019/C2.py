n = int(input())
a = [int(i) for i in input().split()]

import copy


memo = dict()


def search(_accessible, left, maxTurn, _table):
    def write_memo():
        return "".join([c for c in [''.join(map(str, _table[i])) for i in range(3)]])
    if left == 0:  # 探索終了時にスコアを算出して返す
        score = 0
        for _i in range(2):
            for _j in range(3):
                if (_table[_i][_j] == "o" and _table[_i + 1][_j] == "o") \
                        or (_table[_i][_j] == "x" and _table[_i + 1][_j] == "x"):
                    score += b[_i][_j]
        for _i in range(3):
            for _j in range(2):
                if (_table[_i][_j] == "o" and _table[_i][_j + 1] == "o") \
                        or (_table[_i][_j] == "x" and _table[_i][_j + 1] == "x"):
                    score += c[_i][_j]
        return score
    else:
        _writeMemo = write_memo()
        if _writeMemo and (_writeMemo in memo.keys()):
            return memo[_writeMemo]
        _max = -10 ** 10
        _min = 10 ** 10
        for i in range(3):
            for j in range(3):
                if _accessible[i][j]:
                    accessible = copy.deepcopy(_accessible)
                    accessible[i][j] = False
                    table = copy.deepcopy(_table)
                    if maxTurn:
                        table[i][j] = "o"
                        _max = max(_max, search(accessible, left - 1, not maxTurn, table))
                    else:
                        table[i][j] = "x"
                        _min = min(_min, search(accessible, left - 1, not maxTurn, table))
        if maxTurn:
            memo[write_memo()] = _max
            return _max
        else:
            memo[write_memo()] = _min
            return _min

b = [[0 for _ in range(3)] for _ in range(2)]
c = [[0 for _ in range(2)] for _ in range(3)]
for i in range(2):
    b[i] = [int(i) for i in input().split()]
for i in range(3):
    c[i] = [int(i) for i in input().split()]
totalScore = sum(b[0]) + sum(b[1]) + sum(c[0]) + sum(c[1]) + sum(c[2])
_accessible = [[True for _ in range(3)] for _ in range(3)]
_table = [["." for _ in range(3)] for _ in range(3)]
naoki = search(_accessible, 9, True, _table)
print(naoki)
print(totalScore - naoki)
