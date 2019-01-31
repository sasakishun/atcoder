import heapq


def func(n, k, td):
    neta = [0 for _ in range(n)]
    td.sort()
    td.reverse()
    _heapq = []
    _sum = 0
    types = 0
    for i in range(k):
        _sum += td[i][0]
        if neta[td[i][1]] == 0:
            types += 1
        if neta[td[i][1]] > 0:  # 被っているものだけ後で削除する可能性あり
            heapq.heappush(_heapq, td[i])
        neta[td[i][1]] += 1
    _max = _sum + types**2
    # print("td:{} heapq:{}".format(td, _heapq))
    for i in range(k, n):
        # neta[td[i][1]] != 0なら,
        # td[i] < td[j](j<i)なのでtd[i]は無視
        if len(_heapq) > 0 and neta[td[i][1]] == 0:  # 種類が増えるとき
            tmp = heapq.heappop(_heapq)
            _sum -= tmp[0]
            _sum += td[i][0]
            neta[tmp[1]] -= 1
            types += 1
            neta[td[i][1]] += 1
        # print("td:{} heapq:{}".format(td, _heapq))
        # print("_sum:{} typed:{}".format(_sum, types))
        _max = max(_max, _sum + types**2)
    return str(_max)


n, k = [int(i) for i in input().split()]
td = [[0, 0] for _ in range(n)]
for i in range(n):
    td[i][1], td[i][0] = [int(i) for i in input().split()]
    td[i][1] -= 1
# print("print(func({},{},{}))".format(n, k, td))
print(func(n, k, td))
"""
print(func(5,3,[[9, 0], [7, 0], [6, 1], [5, 1], [1, 2]]))
print(func(7,4,[[1, 0], [1, 1], [1, 2], [6, 3], [5, 3], [5, 3], [5, 3]]))
print(func(6,5,[[1000000000, 4], [990000000, 1], [980000000, 2], [970000000, 5], [960000000, 5], [950000000, 3]]))
"""
