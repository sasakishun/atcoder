import math

q, h, s, d = [20, 30, 70, 90] # [int(i) for i in input().split()]
n = 3 # int(input())
size = [0.25, 0.5, 1., 2.]
money = [q, h, s, d]
# 全探索は不可能、理論的に算出
# 単位量当たりの価格を算出
# まず0.25Lずつ買うといくらになるのか算出
# このうちいくらかを0.5Lで置き換えて、安くなるか判断

# 最もコスパがいいもので買い、超過分を別のリットルで置き換える
# これを置き換えられなくなるまで行う

# まず最高コスパで算出
minMoney = 0
nowL = 0
maxPerformance = 0
maxPerformanceIndex = 0
for i in range(4):
    if maxPerformance < size[i] / money[i]:
        maxPerformance = size[i] / money[i]
        nowL = math.ceil(n/size[i]) * size[i]
        minMoney = nowL * money[i]
        maxPerformanceIndex = i
print("nowL:{} maxPerformance:{}, minMoney:{} maxIndex:{}".
      format(nowL, maxPerformance, minMoney, maxPerformanceIndex))
over = nowL - size[maxPerformanceIndex]
print("over:{}".format(over))