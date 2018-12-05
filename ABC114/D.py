n = int(input())


# 入力 : 自然数     ex) 12
# 出力 : 約数リスト ex) [(2,2),(3,1)]
def factorize(n):
    fct = []  # prime factor
    b, e = 2, 0  # base, exponent
    while b * b <= n:
        while n % b == 0:
            n = n // b
            e = e + 1
        if e > 0:
            fct.append((b, e))
        b, e = b + 1, 0
    if n > 1:
        fct.append((n, 1))
    return fct


divList = [0 for i in range(n + 1)]
# divList[1] = 1
for i in range(2, n + 1):
    tmp = factorize(i)
    for j in range(len(tmp)):
        divList[tmp[j][0]] += tmp[j][1]
# print(divList)
# print(sum())
count = 0

# a^d * b^e * c^fの約数は(d+1)*(e+1)*(f+1)個
# つまり75個約数があるとは
# 3*5*5=(2+1)*(4+1)*(4+1)
# 3*25=(2+1)*(24+1)
# 5*15=(4+1)*(14+1)
# 75=(74+1)
# よって各約数を数えればいいだけ
for i in range(len(divList) - 2):
    for j in range(i + 1, len(divList) - 1):
        for k in range(j + 1, len(divList)):
            if divList[i] >= 2 and divList[j] >= 4 and divList[k] >= 4:
                # print("i:{} j:{} k:{} sum:{}".format(i, j, k, (i ** 2) * (j ** 4) * (k ** 4)))
                count += 1
            if divList[i] >= 4 and divList[j] >= 2 and divList[k] >= 4:
                # print("i:{} j:{} k:{} sum:{}".format(i, j, k, (i ** 4) * (j ** 2) * (k ** 4)))
                count += 1
            if divList[i] >= 4 and divList[j] >= 4 and divList[k] >= 2:
                # print("i:{} j:{} k:{} sum:{}".format(i, j, k, (i ** 4) * (j ** 4) * (k ** 2)))
                count += 1
for i in range(len(divList) - 1):
    for j in range(i + 1, len(divList)):
        if (divList[i] >= 2 and divList[j] >= 24):
            # print("i:{} j:{} sum:{}".format(i, j, (i ** 2) * (j ** 24)))
            count += 1
        if (divList[i] >= 24 and divList[j] >= 2):
            # print("i:{} j:{} sum:{}".format(i, j, (i ** 24) * (j ** 2)))
            count += 1
        if (divList[i] >= 14 and divList[j] >= 4):
            # print("i:{} j:{} sum:{}".format(i, j, (i ** 14) * (j ** 4)))
            count += 1
        if divList[i] >= 4 and divList[j] >= 14:
            # print("i:{} j:{} sum:{}".format(i, j, (i ** 4) * (j ** 14)))
            count += 1
for i in range(len(divList)):
    if divList[i] >= 74:
        # print("i:{} sum:{}".format(i, (i ** 74)))
        count += 1
print(count)