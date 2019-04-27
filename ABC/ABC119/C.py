def func(n, a, b, c, l):
    # 連結後に増加させても、連結前に増加させてもコストは変わらない
    # 全通り試す（各l[i]をa,b,c,非使用で4分割し
    # そのあといくらコストがかかるか計算）
    def search(now, cost):
        if len(now) == len(l):
            _a = []
            _b = []
            _c = []
            for i in range(len(now)):
                if now[i] == 0:
                    _a.append(l[i])
                elif now[i] == 1:
                    _b.append(l[i])
                elif now[i] == 2:
                    _c.append(l[i])
            if not _a or not _b or not _c:
                return 10**10
            _cost = abs(a - sum(_a)) + abs(b - sum(_b)) + abs(c - sum(_c))
            _cost += (len(_a) - 1 + len(_b) - 1 + len(_c) - 1) * 10
            return _cost
        else:  # まだ分類していないl[i]がある場合
            for i in range(4):
                cost = min(cost, search(now+[i], cost))
            return cost
    cost = search([], 10**10)
    return cost

n, a, b, c = [int(i) for i in input().split()]
a, b, c = sorted([a, b, c])
l = []
for i in range(n):
    l.append(int(input()))
# print("a:{} b:{} c:{}".format(a, b, c))
# print("{}, {}, {}, {}, {}".format(n, a, b, c, sorted(l)))
print(func(n, a, b, c, l))
"""
print(func(5, 80, 90, 100, [21, 30, 40, 80, 98]))
print(func(8, 80, 90, 100, [80, 80, 80, 90, 90, 90, 100, 100]))
print(func(5, 100, 800, 1000, [300, 333, 400, 444, 500, 555, 600, 666]))
"""