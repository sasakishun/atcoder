def func(k):
    return


def sunuke():
    sn = [0 for _ in range(10 ** 6)]
    _min = [10 ** 10 for _ in range(len(sn))]
    prevMin = 10 ** 5
    for i in reversed(range(1, len(sn))):
        _sum = 0
        _str = str(i)
        for j in range(len(_str)):
            _sum += int(_str[j])
        sn[i] = i / _sum
        if sn[i] < prevMin:
            _min[i] = i / _sum
            prevMin = i / _sum
        else:
            _min[i] = prevMin
            # print("n:{} s(n):{} n/s(n):{}".format(i, _sum, i/_sum))
    for i in range(1, len(sn) - 1):
        if sn[i] <= _min[i + 1]:
            print("n:{} sn:{} upperMin:{}".format(i, sn[i], _min[i + 1]))


k = 30  # input()
now = 1
counter = 1
while counter <= k:
    if counter <= 27:
        print(now)
        if counter % 9 != 0:
            now += 10 ** (len(str(now))-1)
        else:
            now += 10 ** len(str(now))
    else:
        print("2nd phase")
        print(now)
        now += 1
    counter += 1