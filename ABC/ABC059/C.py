n = int(input())
a = [int(i) for i in input().split()]
imos = [i for i in a]
prev = 0
count = 0
# 先頭を正にする場合
for i in range(1, n):
    imos[i] += imos[i - 1] + prev
    print("i:{} prev:{} {}".format(i, prev, imos))
    if imos[i - 1] < 0 and imos[i] <= 0:
        prev += -imos[i] + 1
        count += -imos[i] + 1
        print(-imos[i]+1)
        imos[i] = 1
    elif imos[i - 1] > 0 and imos[i] >= 0:
        prev += -imos[i] - 1
        count += imos[i] + 1
        print(imos[i]+1)
        imos[i] = -1
    print("i:{} prev:{} {}\n".format(i, prev, imos))
print(imos)
print(count)
