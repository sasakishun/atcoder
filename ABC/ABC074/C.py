a, b, c, d, e, f = [int(i) for i in input().split()]
waterA = [a * 100 * i for i in range(int(f / (100 * a)) + 1)]
waterB = [b * 100 * i for i in range(int(f / (100 * b)) + 1)]
sugarC = [c * i for i in range(int(f / c) + 1)]
sugarD = [d * i for i in range(int(f / d) + 1)]

# まず水が何100gにできるかを算出(<F)
_water = []
for i in range(len(waterA)):
    for j in range(len(waterB)):
        if 100 * a * i + 100 * b * j <= f:
            _water.append(100 * a * i + 100 * b * j)
_water = sorted(_water)[1:]
water = [_water[0]]
for i in range(1, len(_water)):
    if _water[i] != _water[i - 1]:
        water.append(_water[i])
# 砂糖が何gにできるかを算出(<F)
_sugar = []
for i in range(len(sugarC)):
    for j in range(len(sugarD)):
        if c * i + d * j <= f:
            _sugar.append(c * i + d * j)
_sugar = sorted(_sugar)
sugar = [_sugar[0]]
for i in range(1, len(_sugar)):
    if _sugar[i] != _sugar[i - 1]:
        sugar.append(_sugar[i])
# print(water)
# print(sugar)
# 各場合で砂糖の最大量を計算
maxSugar = [-1, -1, -1]  # [dense, sugar, total]
for i in range(len(sugar)):
    for j in range(len(water)):
        if sugar[i] + water[j] > f:
            continue
        elif maxSugar[0] < sugar[i]/(sugar[i]+water[j]) <= e/(100+e):
            maxSugar[0] = sugar[i]/(sugar[i]+water[j])
            maxSugar[1] = sugar[i]
            maxSugar[2] = sugar[i] + water[j]
        # print("s:{} w:{} dense:{}".format(sugar[i], water[j], sugar[i]/(sugar[i]+water[j])))
# print(e/(100+e))
if maxSugar[0] == -1:
    print("1 0")
else:
    print("{} {}".format(maxSugar[2], maxSugar[1]))
