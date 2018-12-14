import math

q, h, s, d = [int(i) for i in input().split()]
n = int(input())
size = [0.25, 0.5, 1., 2.]
money = [[0.25 / q, q, 0.25], [0.5 / h, h, 0.5],
         [1 / s, s, 1.], [2 / d, d, 2.]]
# コスパ高い順にソート
money = list(reversed(sorted(money)))
# print(money)
totalMoney = 0
while True:
    totalMoney += int(n / money[0][2]) * money[0][1]
    # print("add:{} {}cup {}yen".format(int(n / money[0][2]) * money[0][1], int(n / money[0][2]), money[0][1]))
    n %= money[0][2]
    # print("totalmoney:{}".format(totalMoney))
    if n == 0:
        print(totalMoney)
        exit()
    del money[0]

"""
leftFlag = True
while True:
    # 確定分のお金を加算
    totalMoney += int(n/money[0][2])*money[0][1]
    print("add:{} {}cup {}yen".format(int(n/money[0][2])*money[0][1], int(n/money[0][2]), money[0][1]))
    n %= money[0][2]
    print("totalmoney:{}".format(totalMoney))
    if n == 0:
        print(totalMoney)
        exit()
    # [お金, どの容器か(q,h,s,d)]
    over = [money[0][1], money[0][2]]
    moreGoodExist = False
    for i in range(1, len(money)):
        if math.ceil(n/money[i][2])*money[i][1] < over[0]:
            over =[math.ceil(n/money[i][2])*money[i][1], money[i][2]]
            moreGoodExist = True
    if moreGoodExist:
        del money[0]
    else:
        print(totalMoney + over[0])
        exit()
"""