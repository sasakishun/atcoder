def func(n, a, x):
    # x.sort()
    dp = [[[0] * (sum(x) + 1)
           for _ in range(n + 1)]
          for _ in range(n)]
    # dp = [[[0] * (sum(x) + 1)] * (n + 1) for _ in range(n)]
    """
    dp = [[[0 for _ in range(sum(x) + 1)]
           for _ in range(n + 1)]
          for _ in range(n)]
    """
    """
    print(len(dp))
    print(len(dp[0]))
    print(len(dp[0][0]))
    print(dp)
    print(dp[0])
    print(dp[0][0])
    """
    # table[j][k][s] = x[j+1]までからk枚選んで、その和がsの場合の数
    # 0 <= j < N, 0 <= k <= N, s <= sum(x)
    # jはインデックスだが,kは選ぶ枚数なので「j < n」「k < n + 1」
    # dp[j][k][s] = dp[j-1][k][s] # x[j]を選ばないとき
    #               + dp[j-1][k-1][s-x[j]] #x[j]を選ぶ場合 (ただし1<=j<=k)
    # dp[0][0][0] = 1 #初期値(シード的な)
    # dp = 0 # 上記以外の場合
    dp[0][0][0] = 1
    # j == 0 での処理
    dp[0][1][x[0]] = 1

    for j in range(1, len(dp)):
        for k in range(len(dp[0])):
            for s in range(len(dp[0][0])):
                # 「j == 0」での事前処理が必要
                # if j > 0: # 解説では j > 0 and x[j] >= sらしい
                dp[j][k][s] += dp[j - 1][k][s]
                if k > 0 and s >= x[j]:
                    dp[j][k][s] += dp[j - 1][k - 1][s - x[j]]
                    # print("dp[{}][{}][{}]:{} <- dp[{}][{}][{}]:{} + {}".format(
                    # j, k, s, dp[j][k][s], j-1, k-1, s-x[j], dp[j-1][k-1][s-x[j]], x[j]))
                    # if dp[j][k][s] > 0:
                    # print("dp[{}][{}][{}]:{}---------------".format(j, k, s, dp[j][k][s]))
                    # else:
                    # print("dp[{}][{}][{}]:{}".format(j, k, s, dp[j][k][s]))
                    # for k in range(len(dp[0])):
                    # for j in range(len(dp)):
                    # print(dp[j][k])
    count = 0
    for k in range(1, min(len(dp[0]), len(dp[0][0]) // a + 1)):
        # print("dp[{}][{}][{}]:{}".format(n - 1, k, a * k, dp[n - 1][k][a * k]))
        count += dp[n - 1][k][a * k]
    return count


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
