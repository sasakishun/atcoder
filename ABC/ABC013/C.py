import math

n, _h = [int(i) for i in input().split()]
a, b, c, d, e = [int(i) for i in input().split()]

# aが何日間か決まればc,eが何日間は自動で決定できる
minMoney = 0
firstFlag = True
for i in range(n + 1):  # aがi日間
    h = _h
    money = a * i
    h += b * i
    # cについて
    beta = max(0, math.ceil(((n - i) * e - h) / (e + d)))
    if ((n - i) * e - h) / (e + d) >= 0 and \
                    math.ceil(((n - i) * e - h) / (e + d)) == int(((n - i) * e - h) / (e + d)):
        beta += 1
    # print("e:{} n-i:{} h:{} d+e:{}".format(e, n-i, h, d + e))
    # print(((n - i) * e - h) / (e + d))
    money += beta * c
    h += beta * d
    h -= e * (n - i - beta)
    # print("a:{} c:{} e:{} h:{} money:{}".format(i, beta, n - i - beta, h, money))

    if h > 0:
        if firstFlag:
            minMoney = money
            firstFlag = False
        else:
            minMoney = min(minMoney, money)
print(minMoney)
