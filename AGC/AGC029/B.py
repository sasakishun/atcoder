def search(_a, tmp):
    while _a >= 2 ** tmp:
        tmp += 1
    return tmp


def func(n, a):
    # a[i] + a[j] = 2^tとなる組の最大数
    a.sort()
    a.reverse()
    available = [True for _ in range(len(a))]
    # print(a)
    # diff = [search(a[i]) - a[i] for i in range(len(a))]
    diff = [[0, i] for i in range(len(a))]
    tmp = 0
    for i in reversed(range(len(diff))):
        tmp = search(a[i], tmp)
        diff[i][0] = 2 ** tmp - a[i]
    diff.sort()
    # a.reverse()
    diff.reverse()
    i = 0
    j = 0
    count = 0
    while i < len(a) and j < len(diff):
        while j < len(diff) and (diff[j][0] > a[i] or not available[diff[j][1]]):
            j += 1
        while i < len(a) and not available[i]:
            i += 1
        # print("i:{} j:{} count:{} avail:{}".format(i, j, count, available))
        if i < len(a) and j < len(a) and a[i] == diff[j][0]:
            if i != diff[j][1]:
                count += 1
                available[i] = False
                available[diff[j][1]] = False
                i += 1
                # if i > 0 and a[i - 1] == a[i] and i == diff[j][1]:
                # i += 1
                j += 1
            else:
                j += 1
        else:
            i += 1
    # print("   a:{}".format(a))
    # print("diff:{}".format(diff))
    return count


n = int(input())
a = [int(i) for i in input().split()]
print("{}".format(func(n, a)))
# print("{}".format(func(3, [1, 2, 3])))
# print("{}".format(func(5, [3, 11, 14, 5, 13])))
# print("{}".format(func(3, [1, 3, 29, 35])))
# print("{}".format(func(5, [1, 2, 2, 2, 2])))
# print("{}".format(func(6, [1, 2**50-1])))
# print("{}".format(func(7, [1, 7, 7, 25, 63, 127, 127])))
# print("{}".format(func(4, [1, 1, 2, 3])))
