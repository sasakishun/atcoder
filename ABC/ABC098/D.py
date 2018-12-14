# print(2*10**5 / 2**17)
# exit()
# n = 4
# a = [2, 5, 4, 6]
# n = 9  # int(input())
# a = [0,0,0,0,0,0,0,0,0]  # [int(i) for i in input().split()]
# n = 19
# a = [885, 8, 1, 128, 83, 32, 256, 206, 639, 16, 4, 128, 689, 32, 8, 64, 885, 969, 1]
n = int(input())
a = [int(i) for i in input().split()]

# xorをしても普通に足した時と結果が変わらない
# => xorによる減少がないということ
# => 1が重複する桁がない(必要十分条件)
# => 全桁が1となる

# そしてある区間で条件を満たすとき,その区間には
# 条件を満たさないものはない、つまり尺取り法
digit = [0 for _ in range(20)]


def addDigit(_a):
    j = 0
    while _a > 0:
        if _a % 2 == 1:
            digit[j] += 1
        _a = int(_a / 2)
        j += 1


def diffDigit(_a):
    j = 0
    while _a > 0:
        if _a % 2 == 1:
            digit[j] -= 1
        _a = int(_a / 2)
        j += 1


def evaluate(_i, _j):
    if _i == _j:
        return True
    for i in range(len(digit)):
        if digit[i] > 1:
            return False
    return True


count = 0
i = 0
j = -1
while i < len(a) and j < len(a):
    # a[i] + a[i+1] + .....+a[j]が条件を満たすとする
    # print("1 i:{} j:{} count:{} digit:{}".format(i, j, count, digit))
    j += 1
    while j < len(a):
        # print("j:{}".format(j))
        addDigit(a[j])
        if evaluate(i, j):
            count += j - i + 1
            # print("hit:[{},{}] count:{} digit:{}".format(i, j, count, digit))
            # 条件を満たす限りjをインクリメント
            j += 1
        else:
            # print("break in [{},{}] digit:{}".format(i, j, digit))
            # diffDigit(a[j])
            # j += 1
            break
    # print("2 i:{} j:{} count:{} digit:{}".format(i, j, count, digit))
    while i <= j < len(a):
        # print("i:{}".format(i))
        if not evaluate(i, j):
            # ここが問題、ちゃんと引けてない[3,3]の時など
            diffDigit(a[i])
            i += 1
        else:
            count += j - i + 1
            # print("2nd hit:[{},{}] count:{} digit:{}".format(i, j, count, digit))
            break
    # print("3 i:{} j:{} count:{} digit:{}".format(i, j, count, digit))
# print(digit)
print(count)
"""
sum = [0 for i in range(n)]

count = [1 for i in range(n)]
sum[0] = a[0]

r = 1
while r < n:
    if sum[r - 1] ^ a[r] == sum[r - 1] + a[r]:
        count[r] = count[r - 1] + 1
        sum[r] = sum[r - 1] + a[r]
        print("---------ok")
    else:
        sum[r] = a[r]
    r += 1
    print("")

for i in range(n - 1):
    count[i + 1] += count[i]
print(count[-1])
"""
