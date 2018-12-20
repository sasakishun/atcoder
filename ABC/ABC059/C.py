n = int(input())
a = [int(i) for i in input().split()]

# a[0]の符号を正にするか負にするかの2択で
# 後は一意に決まる

_sum = 0
count = 0
out = 0
# a[0]の符号を正にする場合
for i in range(len(a)):
    if i % 2 == 1:  # a[i]までの和を負にする
        if _sum + a[i] >= 0:
            count += abs(_sum + a[i] - (-1))
            _sum = -1
        else:
            _sum += a[i]
    else:  # a[i]までの和を正にする
        if _sum + a[i] <= 0:
            count += abs(1 - (_sum + a[i]))
            _sum = 1
        else:
            _sum += a[i]
# print("count:{} sum:{}".format(count, _sum))
out = count
_sum = 0
count = 0
# a[0]の符号を負にする場合
for i in range(len(a)):
    if i % 2 == 0:  # a[i]までの和を負にする
        if _sum + a[i] >= 0:
            count += abs(_sum + a[i] - (-1))
            _sum = -1
        else:
            _sum += a[i]
    else:  # a[i]までの和を正にする
        if _sum + a[i] <= 0:
            count += abs(1 - (_sum + a[i]))
            _sum = 1
        else:
            _sum += a[i]
            # print("count:{} sum:{}".format(count, _sum))
print(min(out, count))
