n = int(input())
_max = 0
_sum = 0
for i in range(n):
    p = int(input())
    _sum += p
    if p > _max:
        _max = p
print(_sum - int(_max/2))