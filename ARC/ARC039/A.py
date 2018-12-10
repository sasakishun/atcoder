def listToString(_list, split=""):
    maped_list = map(str, _list)  # mapで要素すべてを文字列に
    mojiretu = split.join(maped_list)
    return mojiretu


a, b = [int(i) for i in input().split()]

_max = -10**5
# aを書き換える場合
for i in range(len(str(a))):
    # 0から9で書き換える
    for j in range(10):
        if i == 0 and j == 0:
            continue
        else:
            tmp = [str(a)[k] for k in range(len(str(a)))]
            tmp[i] = str(j)
            tmp = int(listToString(tmp))
            # print("i:{} j:{} tmp:{}".format(i, j, tmp))
            _max = max(_max, int(tmp) - b)
# bを書き換える場合
for i in range(len(str(a))):
    # 0から9で書き換える
    for j in range(10):
        if i == 0 and j == 0:
            continue
        else:
            tmp = [str(b)[k] for k in range(len(str(b)))]
            tmp[i] = str(j)
            tmp = int(listToString(tmp))
            # print("i:{} j:{} tmp:{}".format(i, j, tmp))
            _max = max(_max, a - int(tmp))
print(_max)