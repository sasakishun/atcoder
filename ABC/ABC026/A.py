a = int(input())
_max = 0
for i in range(0, a+1):
    _max = max(_max, i * (a - i))
print(_max)