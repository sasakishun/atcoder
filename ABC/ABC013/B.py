a = int(input())
b = int(input())
# 0123456789,01234...
_min = 100
if a < b:
    _min = min(_min, a + 10 - b)
    _min = min(_min, b - a)
else:
    _min = min(_min, b + 10 - a)
    _min = min(_min, a - b)
print(_min)
