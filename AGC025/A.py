n = int(input())

minCount = 10 ** 6
for i in range(1, n):
    # a = i, b = n - i として各位の和を計算
    _a = str(i)
    _b = str(n - i)
    count = 0
    for j in range(len(_a)):
        count += int(_a[j])
    for j in range(len(_b)):
        count += int(_b[j])
    minCount = min(minCount, count)
print(minCount)