from operator import itemgetter

def func(n, k, td):
    td.sort()
    last = td[0][0]
    removed = 0
    _sum = []
    i = 0
    td.append([0, 0])
    print(td)
    while i < n - removed + 1:
        if td[i][0] != last:
            td[last:i].sort(key=itemgetter(1))
            _sum.append(td[i-1][1])
            last = td[i][0]
            del td[i-1]
            removed += 1
        else:
            i += 1
    print(td)
    return td
"""
n, k = [int(i) for i in input().split()]
td = [[0, 0] for _ in range(n)]
for i in range(n):
    td[i] = [int(i) for i in input().split()]
# print("print(func({},{},{}))".format(n, k, td))
"""
# print("26 vs " + str(func(5,3,[[1, 9], [1, 7], [2, 6], [2, 5], [3, 1]])))
# print("25 vs " + str(func(7,4,[[1, 1], [2, 1], [3, 1], [4, 6], [4, 5], [4, 5], [4, 5]])))
print("4900000016 vs " + str(func(6,5,[[5, 1000000000], [2, 990000000], [3, 980000000], [6, 970000000], [6, 960000000], [4, 950000000]])))
