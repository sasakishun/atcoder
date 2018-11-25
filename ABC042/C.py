n, k = [int(i) for i in input().split()]
d = [int(i) for i in input().split()]
ok = [1 for i in range(10)]
for i in range(len(d)):
    ok[d[i]] = -1
for i in range(n, 100000):
    complete = True
    for j in range(len(str(i))):
        if ok[int(str(i)[j])] == -1:
            complete = False
            break
    if complete:
        print(i)
        exit()

"""
import copy
def listToString(_list, split=""):
    maped_list = map(str, _list)  # mapで要素すべてを文字列に
    mojiretu = split.join(maped_list)
    return mojiretu

n, k = [int(i) for i in input().split()]
d = [int(i) for i in input().split()]
ok = [1 for i in range(10)]
for i in range(len(d)):
    ok[d[i]] = -1
# nをしたの位から順に置き換えていく
money = [0]
for i in range(len(str(n))):
    money.append(int(str(n)[i]))
# 最小でなくともn以上の整数を作る
for i in reversed(range(1, len(money))):
    for j in range(money[i], 10+money[i]):
        _j = j % 10
        if ok[_j] == 1:
            if _j >= money[i]:
                money[i] = _j
                break
            else:
                money[i] = _j
# print("okList:{}".format(ok))
# print(money)
while True:
    if money[0] != 0:
        break
    else:
        del(money[0])
# print(money)
# 次に可能な限り最小化していく
for i in range(len(money)):
    for j in range(10):
        if ok[j] == 1:
            tmpMoney = copy.deepcopy(money)
            tmpMoney[i] = j
            # print("n:{} tmpMoney:{}".format(n, int(listToString(tmpMoney))))
            if int(listToString(tmpMoney)) >= n:
                # print("money:{}".format(money))
                money[i] = j
                break
print(int(listToString(money)))
"""