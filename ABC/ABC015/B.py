import math

n = int(input())
a = [int(i) for i in input().split()]

count = 0
_sum = 0
for _a in a:
    if _a != 0:
        count += 1
        _sum += _a
print(math.ceil(_sum/count))