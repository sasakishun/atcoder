"""
def func(n, t, v):
    t = [0] + t + [t[-1]]
    print("t:{}".format(t))
    v = [0] + v + [0]

    limit = [0 for _ in range(t[-1] + 1)]
    for i in reversed(range(len(t) - 1)):
        for j in range(t[i] - t[i-1]):
            limit[t[i] - j] = min(v[i + 1] + j, v[i])

    print(limit)
    print([[i, limit[i]] for i in range(len(limit))])
    # print(list(range(len(limit))))
    dist = 0
    prev = 0
    for i in range(1, len(limit)):
        next = min(prev + 1, limit[i])
        dist += (next + prev) / 2
        print("i:{} add:{} dist:{}".format(i, (next + prev) / 2, dist))
        prev = next
    return str(dist)
"""
def func(n, t, v):
    t = [0] + t + [t[-1]]
    v = [0] + v + [0]
    for i in range(len(t)):
        t[i] *= 2
    for i in range(len(v)):
        v[i] *= 2
    # print("t:{}".format(t))

    limit = [0 for _ in range(t[-1] + 1)]
    for i in reversed(range(len(t) - 1)):
        for j in range(t[i] - t[i-1]+1):
            limit[t[i] - j] = min(limit[t[i]] + j, v[i])

    # print(limit)
    # print([[i, limit[i]] for i in range(len(limit))])
    # print(list(range(len(limit))))
    dist = 0
    prev = 0
    for i in range(1, len(limit)):
        next = min(prev + 1, limit[i])
        dist += (next + prev) / 2
        # print("i:{} add:{} dist:{}".format(i, (next + prev) / 2, dist))
        prev = next
    return str(dist/4)

# print(510*510/2)
n = int(input())
t = [int(i) for i in input().split()]
for i in range(1, len(t)):
    t[i] += t[i-1]
v = [int(i) for i in input().split()]
print(func(n, t, v))
# print("print(func({}, {}, {}))".format(n, t, v))
"""
print("2100 vs " + func(1, [100], [30]) + "\n")
print("2632 vs " + func(2, [60, 110], [34, 38]) + "\n")
print("76 vs " + func(3, [12, 26, 28], [6, 2, 7]) + "\n")
print("20.25 vs " + func(1, [9], [10]) + "\n")
print(
    "20291 vs " + func(10, [64, 119, 146, 181, 257, 376, 383, 401, 450, 550], [29, 19, 31, 39, 27, 48, 41, 87, 55, 70]))
"""
