def func(k, a):
    bit = [0 for _ in range(50)]
    for i in range(len(a)):
        binnedA = bin(a[i])[2:]
        _a = [int(binnedA[_i]) for _i in range(len(binnedA))]
        _a.reverse()
        for j in range(len(_a)):
            bit[j] += _a[j]
        # print(bit)
    best = [0 if bit[i] > len(a) - bit[i] else 1 for i in range(len(bit))]
    # print("best:{}".format(best))
    upperBin = bin(k)[2:]
    upper = [int(upperBin[_i]) for _i in range(len(upperBin))]
    upper.reverse()
    for i in range(len(bit)-len(upper)):
        upper.append(0)

    limited = True
    upper.reverse()
    best.reverse()
    # print("upper:{}".format(upper))
    # print("best:{}".format(best))
    for i in range(len(upper)):
        if limited:
            if upper[i] == 1:
                if best[i] == 0:
                    best[i] = 0
                    limited = False
                    # print("unlock:{}".format(i))
                else:
                    best[i] = 1
            else:
                best[i] = 0
    _sum = 0
    best.reverse()
    # print("best:{}".format(best))
    # print("bit:{}".format(bit))
    for i in range(len(best)):
        if best[i] == 0:
            _sum += bit[i] * (2 ** i)
        else:
            _sum += (len(a) - bit[i]) * (2 ** i)
    return _sum
"""
print("func(7, [1, 6, 3]):{}".format(func(7, [1, 6, 3])))
print("func(9, [7, 4, 0, 3]):{}".format(func(9, [7, 4, 0, 3])))
print("func(0, [1000000000000]):{}".format(func(0, [1000000000000])))
"""
n, k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
print(func(k, a))
