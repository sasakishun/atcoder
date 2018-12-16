n = int(input())
_max = 0
out = 1
for i in range(1, n + 1):
    count = 0
    _i = i
    while _i > 0 and _i % 2 == 0:
        count += 1
        _i = _i // 2
    if count > _max:
        out = i
        _max = max(_max, count)
print(out)
