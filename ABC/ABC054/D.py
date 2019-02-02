class abc054D:
    def __init__(self, n, a, b, thing):
        self.n = n
        self.a = a
        self.b = b
        self.thing = thing
        _sumA = 0
        _sumB = 0
        for i in range(len(thing)):
            _sumA += thing[i][0]
            _sumB += thing[i][1]
        self.table = [[[float("inf") for _ in range(_sumB)] for _ in range(_sumA)] for _ in range(n+1)]

    def func(self):
        self.table[0][0][0] = 0
        for i in range(1, len(self.table)):
            for sumA in range(len(self.table[0])):
                for sumB in range(len(self.table[0][0])):
                    if sumA - self.thing[i-1][0] >= 0 and sumB - self.thing[i-1][1] >= 0:
                        self.table[i][sumA][sumB] \
                            = min(self.table[i - 1][sumA][sumB],
                                  self.table[i - 1][sumA - self.thing[i-1][0]][sumB - self.thing[i-1][1]]
                                  + self.thing[i-1][2])
                    else:
                        self.table[i][sumA][sumB] = self.table[i-1][sumA][sumB]
        _min = float("inf")
        for sumA in range(1, len(self.table[0])):
            for sumB in range(1, len(self.table[0][0])):
                if sumA / sumB == self.a / self.b:
                    _min = min(_min, self.table[-1][sumA][sumB])
        if _min == float("inf"):
            return str(-1)
        else:
            return str(_min)

n, a, b = [int(i) for i in input().split()]
thing = [[0, 0, 0] for _ in range(n)]
for i in range(n):
    thing[i] = [int(i) for i in input().split()]
print(abc054D(n, a, b, thing).func())
"""
# print("print(\" vs \" + func({}, {}, {}, {}))".format(n, m, a, thing))
print("3  vs " + abc054D(3, 1, 1, [[1, 2, 1], [2, 1, 2], [3, 3, 10]]).func())
print("-1 vs " + abc054D(1, 1, 10, [[10, 10, 10]]).func())
"""
