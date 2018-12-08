import math

n = int(input())
a = [0 for _ in range(n)]
b = [0 for _ in range(n)]
for i in range(n):
    a[i], b[i] = [int(i) for i in input().split()]
# print(a)
# print(b)
# a[i]のボタンを押すとa[0]からa[i]まですべてが+1
# 上位から決めていけばよい
add = 0
for i in reversed(range(n)):
    # a[i]がb[i]の倍数,つまりa[i] = b[i] * k
    # a[i] = b[i] * math.ceil(a[i] / b[i])
    a[i] += add
    add += b[i] * math.ceil(a[i] / b[i]) - a[i]
# print(a)
print(add)