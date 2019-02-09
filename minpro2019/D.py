def func(l, a):
    # スタートを0としてiまで歩く時に減らせるコスト
    imos = [0 for _ in range(l+1)]
    res = [0 for _ in range(l)]
    for i in range(1, l+1):
        if a[i-1] % 2 == 1:
            imos[i] = imos[i - 1] + a[i - 1]
            res[i-1] = 0
        else:
            imos[i] = imos[i - 1] + a[i - 1] - 1
            if a[i-1] == 0:
                res[i-1] = 0
            else:
                res[i-1] = 1
    print("a:{}".format(a))
    print("imos:{}".format(imos))
    print("res:{}".format(res))

    # 終端から戻ってくるまでに消費できるコスト
    _sum = [0 for _ in range(l+1)]
    for i in reversed(range(l-1)):
        if res[i] == 1:
            _sum[i] = _sum[i+1] + 1
        else:
            _sum[i] = max(0, _sum[i+1] - 1)
    print("_sum:{}\n".format(_sum))
    _max = 0
    _min = float("inf")
    for i in range(1, len(imos)):
        _min = min(_min, imos[i])
        _max = max(_max, imos[i] - _min + _sum[i-1])
    return sum(a) - _max
"""
l = int(input())
a = [0 for _ in range(l)]
for i in range(l):
    a[i] = int(input())
print(min(func(l, a), func(l, list(reversed(a)))))
"""
# print("print(\"vs \" + str(func({}, {})))".format(l, a))
print("1 vs " + str(min(func(4, [1, 0, 2, 3]), func(4, list(reversed([1, 0, 2, 3]))))))
print("3 vs " + str(min(func(8, [2, 0, 0, 2, 1, 3, 4, 1]), func(8, list(reversed([2, 0, 0, 2, 1, 3, 4, 1]))))))
print("1 vs " + str(min(func(7, [314159265, 358979323, 846264338, 327950288, 419716939, 937510582, 0]),
                        func(7, list(reversed([314159265, 358979323, 846264338, 327950288, 419716939, 937510582, 0]))))))
