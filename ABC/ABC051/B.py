import math

n = int(input())
a = [0 for _ in range(n)]
for i in range(n):
    a[i] = int(input())
a.sort()
a.reverse()
_sum = 0
for i in range(len(a)):
    if i % 2 == 0:
        _sum += a[i] ** 2
    else:
        _sum -= a[i] ** 2
print(_sum * math.pi)