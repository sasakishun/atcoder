import math


class binarySearch:
    # 添え字「t」によってソート済みリストを二分探索
    def __init__(self, limit, target):
        self.limit = limit
        self.target = target
        self.t = 0

    def condition(self, h, a, b):
        if self.t < 0:
            return False
        count = 0
        for i in range(len(h)):
            if h[i] > b * self.t:
                count += math.ceil((h[i] - b * self.t) / (a - b))
        if count > self.t:
            return False
        else:
            return True

    def search(self, h, a, b):
        low = 0
        high = self.limit
        self.t = int((low + high) / 2)
        while high >= low:
            out = self.condition(h, a, b)
            # print("t:{} _out:{} limit:{}\n".format(t, out, self.limit))
            if not out:
                low = self.t + 1
            else:
                high = self.t - 1
            self.t = int((low + high) / 2)
        # print("low:{} high:{} t:{}".format(low, high, self.t))
        return self.t + 1


def func(a, b, _h):
    _h.sort()
    _h.reverse()
    _sum = 0  # 現在何回以上爆発させることが確定しているか
    aMargin = 0  # _sum回のうちあと何回aを使うことができるか
    for h in _h:
        print("prev cost upper:{}".format(a * aMargin + b * (_sum - aMargin)))
        # まず_sum回で抑える場合にaがいくつ必要か算出
        if h <= a * aMargin + b * (_sum - aMargin):
            # そのうちどれだけaを使わないでいられるか
            h -= b * _sum  # まず必ず減る部分を計算
            if h > 0:
                aMargin -= math.ceil(h / (a - b))  # a が何回必要か
        else:
            # hを0にするのに必要最低限の回数をを算出
            tmpH = h
            tmpH -= a * aMargin + b * (_sum - aMargin)
            extra = math.ceil(tmpH / a)
            _sum += extra
            aMargin += extra
            print("aMargin:{}".format(aMargin))
            # 合計して「_sum」回が最小回数
            # ここで使えるaは「aMargin」回
            # そのうちどれだけaを使わないでいられるか
            h -= b * _sum  # まず必ず減る部分を計算
            aMargin -= math.ceil(h / (a - b))  # a が何回必要か
        print("_sum:{} margin:{}".format(_sum, aMargin))
    return str(_sum)


n, a, b = [int(i) for i in input().split()]
h = [0 for _ in range(n)]
for i in range(n):
    h[i] = int(input())
# print(func(a, b, h))
binary = binarySearch(target=math.ceil(max(h) / a), limit=math.ceil(max(h) / 1))
print(binary.search(h, a, b))
# print("print(func({}, {}, {}))".format(a, b, h))
"""
print("2 vs " + func(5, 3, [8, 7, 4, 2]))
print("4 vs " + func(10, 4, [20, 20]))
print("800000000 vs " + func(2, 1, [900000000, 900000000, 1000000000, 1000000000, 1000000000]))
"""
