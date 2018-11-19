n = int(input())
f = [[0 for j in range(10)] for i in range(n)]
p = [[0 for i in range(11)] for j in range(n)]
for i in range(n):
    f[i] = [int(i) for i in input().split()]
for i in range(n):
    p[i] = [int(i) for i in input().split()]

totalProfit = 0
N = [i for i in range(10)]  # N = bit探索する桁数
for i in range(1, 1 << len(N)):
    output = []
    for j in range(len(N)):
        if ((i >> j) & 1) == 1:
            output.append(j)  # このjが今回探索するindexの1つ
    profit = 0
    for j in range(n):
        sameOpen = 0
        for k in output:
            if f[j][k] == 1:  # 店j,曜日時間帯kと営業日被り
                sameOpen += 1
        profit += p[j][sameOpen]
        # print("store:{} sameOpen:{}".format(j, sameOpen))
    # print("profit:{} {}".format(profit, output))
    if i == 1:
        totalProfit = profit
    else:
        totalProfit = max(totalProfit, profit)
print(totalProfit)
