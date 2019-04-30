n, m = [int(i) for i in input().split()]
a = [[0, 0] for _ in range(n)]
for i in range(n):
    a[i] = [int(i) for i in input().split()]
a.sort()
_sum = 0
for i in range(len(a)):
    _sum += a[i][0] * min(m, a[i][1])
    m -= min(m, a[i][1])
print(_sum)