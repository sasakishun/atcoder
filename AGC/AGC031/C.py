def listToString(_list, split=""):
    maped_list = map(str, _list)  # mapで要素すべてを文字列に
    mojiretu = split.join(maped_list)
    return mojiretu

def binToInt(_bin):
    out = 0
    for i in range(len(_bin)):
        out += (2**i)*_bin[i]
    return out

n, a, b = [int(i) for i in input().split()]
_a = str(bin(a))[2:]
_b = str(bin(b))[2:]
a = [int(_a[i]) for i in reversed(range(len(_a)))]
b = [int(_b[i]) for i in reversed(range(len(_b)))]
# 長さをそろえる
for i in range(len(a) - len(b)):
    b.append(0)
for i in range(len(b) - len(a)):
    a.append(0)
hamDis = 0
for i in range(len(a)):
    if a[i] != b[i]:
        hamDis += 1
# print("hamDis:{}".format(hamDis))
if hamDis <= 2 ** n - 1 and (2 ** n - 1 - hamDis) % 2 == 0:
    print("YES")
    _a = binToInt(a)
    out = [_a]
    for i in range(len(a)):
        if a[i] != b[i]:
            if a[i] == 0:
                _a += 2 ** i
            else:
                _a -= 2 ** i
            out.append(_a)
    margin = 2 ** n - 1 - hamDis
    tmp = 2 ** 30
    for i in range(margin):
        if i % 2 == 0:
            _a += tmp
        else:
            _a -= tmp
        out.append(_a)
    print(listToString(out, " "))
    # for i in out:
        # print(bin(i)[2:])
else:
    print("NO")