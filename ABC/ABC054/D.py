class abc054D:
    def __init__(self, n, a, b, thing):
        self.n = n
        self.a = a
        self.b = b
        self.thing = thing
        self.table = [[[float("inf") for _ in range(400)] for _ in range(400)] for _ in range(n)]

    def func(self):
        for sumA in range(len(self.table[0])):
            for sumB in range(len(self.table[0][0])):
                if sumA > 0 and sumB > 0 and sumA / sumB == self.a / self.b:
                    self.table[0][sumA][sumB] = 0

        for i in range(1, len(self.table)):
            for sumA in range(len(self.table[0])):
                for sumB in range(len(self.table[0][0])):
                    # print("i;{} sumA:{} sumB:{}".format(i, sumA, sumB))
                    self.table[i][sumA][sumB] \
                        = min(self.table[i - 1][sumA][sumB],
                              self.table[i - 1][sumA - self.thing[i][0]][sumB - self.thing[i][1]] + self.thing[i][2])
        for i in range(len(self.table)):
            for sumA in range(len(self.table[0])):
                for sumB in range(len(self.table[0][0])):
                    if self.table[i][sumA][sumB] != float("inf"):
                        print("table[{}][{}][{}]:{}".format(i, sumA, sumB, self.table[i][sumA][sumB]))
        return str(min(self.table[0][0][0],
                       self.table[0][self.thing[0][0]][self.thing[0][1]]
                       + self.thing[0][2]))


"""
n, m, a = [int(i) for i in input().split()]
thing = [[0, 0, 0] for _ in range(n)]
for i in range(n):
    thing[i] = [int(i) for i in input().split()]
"""
# print("print(\" vs \" + func({}, {}, {}, {}))".format(n, m, a, thing))
print("3  vs " + abc054D(3, 1, 1, [[1, 2, 1], [2, 1, 2], [3, 3, 10]]).func())
# print("-1 vs " + abc054D(1, 1, 10, [[10, 10, 10]]).func())
