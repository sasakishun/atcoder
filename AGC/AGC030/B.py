import copy


"""
l, n = [10, 6]
x = [1, 2, 3, 6, 7, 9]
"""
l, n = [int(i) for i in input().split()]
x = [0 for _ in range(n)]
for i in range(n):
    x[i] = int(input())
x.sort()
"""
x = queue.Queue
for i in range(n):
    x.get(_x[i])
"""
"""
count = 0
prev = 0
while len(x) > 0:
    if prev <= x[0] <= x[-1]:
        if x[0] - prev > prev + l - x[-1]:
            count += x[0] - prev
            prev = x[0]
            x = x[1:]
        else:
            count += prev + l - x[-1]
            prev = x[-1]
            x = x[:-1]
    elif x[0] <= prev <= x[-1]:
        if prev - x[0] >= x[-1] - prev:
            count += prev - x[0]
            prev = x[0]
            x = x[1:]
        else:
            count += x[-1] - prev
            prev = x[-1]
            x = x[:-1]
    else:
        if prev - x[-1] > x[0] + l - prev:
            count += prev - x[-1]
            prev = x[-1]
            x = x[:-1]
        else:
            count += x[0] + l - prev
            prev = x[0]
            x = x[1:]
    print("x:{} prev:{} count:{}".format(x, prev, count))
"""

def right(i, j):
    # iからjまでの時計回りの距離
    if i < j:
        return i + l - j
    else:
        return i - j

def left(i, j):
    # iからjまでの反時計回りの距離
    if i < j:
        return j - i
    else:
        return j + l - i

_max = 0
for i in range(1, n-1):
    # x[i],x[i+1]は通らない
    # x[i+1]->x[i-1]->x[i+2]->x[i-2]
    _x = copy.deepcopy(x)
    _x = _x[i+2:n]+_x[0:i+1]
    # print(_x)
    count = 0
    prev = x[i+1]
    while len(_x) > 0:
        #print("i:{} count:{} prev:{}".format(i, count, prev))
        count += left(prev, _x[-1])
        prev = _x[-1]
        _x = _x[:-1]
        if len(_x) > 0:
            # print("i:{} count:{} prev:{}".format(i, count, prev))
            count += right(prev, _x[0])
            prev = _x[0]
            _x = _x[1:]
    # print("i:{} count:{}".format(i, count + min(abs(l - prev), prev)))
    _max = max(_max, count + min(abs(l - prev), prev))

    """
    _x = copy.deepcopy(x)
    _x = _x[i+3:n]+_x[0:i+2]
    count = 0
    prev = x[i]
    while len(_x) > 0:
        # print("i:{} count:{} prev:{}".format(i, count, prev))
        count += right(prev, _x[0])
        prev = _x[0]
        _x = _x[1:]
        if len(_x) > 0:
            # print("i:{} count:{} prev:{}".format(i, count, prev))
            count += left(prev, _x[-1])
            prev = _x[-1]
            _x = _x[:-1]
    print("i:{} count:{}".format(i, count + min(abs(l - prev), prev)))
    _max = max(_max, count + min(abs(l - prev), prev))
    """
print(_max)