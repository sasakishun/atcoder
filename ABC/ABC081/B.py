n = int(input())
a = [int(i) for i in input().split()]
_min = 10**5
for _a in a:
    count = 0
    while _a > 0 and _a % 2 == 0:
        count += 1
        _a = _a // 2
    _min = min(_min, count)
print(_min)