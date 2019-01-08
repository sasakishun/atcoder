def func(n, a, x):
    # NX
    # x.sort()
    x = [i - a for i in x]
    minus = 0
    plus = 0
    for _x in x:
        if _x > 0:
            plus += _x
        else:
            minus += _x
    # print("x:{}".format(x))
    dp = [[0] * (plus - minus + 1) for j in range(n + 1)]
    # 平均がAとは,x[i]-Aの和が0となること
    # dp[j][t] = "xからj枚以上選んで和が「t-(負のxの和)」の場合の数"
    # 0 <= j <= N
    # 0 <= t <= (正のx[i]-Aを全て選ぶ) - (負のx[i]-Aを全て選ぶ)
    # dp[j][t] = dp[j-1][t-x[j]] + dp[j-1][t]
    # dp[0][-(負のxの和)] = 1 #初期シード,1つも選ばない場合は1通り
    # dp[0][-(負のxの和)でない] = 0
    dp[0][-minus] = 1
    for j in range(1, len(dp)):
        for t in range(len(dp[0])):
            # print("j:{} dp({},{})".format(j, len(dp), len(dp[0])))
            dp[j][t] = dp[j - 1][t]
            # print("t:{} x[{}]:{}".format(t, j-1, x[j-1]))
            if len(dp[0]) > t - x[j-1] >= 0:
                # print(t - x[j-1])
                dp[j][t] += \
                    dp[j - 1][t - x[j-1]]
    return dp[n][-minus] - 1


n, a = [int(i) for i in input().split()]
x = [int(i) for i in input().split()]
print(func(n, a, x))
"""
print(func(4, 8, [7, 8, 9, 9]) == 5)  # 合計33
print(func(3, 8, [6, 6, 9]) == 0)  # 合計21
print(func(8, 5, [3, 6, 2, 8, 7, 6, 5, 9]) == 19)  # 合計46
print(func(33, 3,
           [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3])
      == 8589934591)  # 合計46
"""
