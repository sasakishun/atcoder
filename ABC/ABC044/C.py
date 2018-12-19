def func(n, a, x):
    dp = [[[0 for _ in range(sum(x))] for _ in range(n)] for _ in range(n)]
    # table[j][k][s] = x[j]までからk枚選んで、その和がsの場合の数
    # dp[j][k][s] = dp[j-1][k][s] # x[j]を選ばないとき
    #               + dp[j-1][k-1][s-x[j]] #x[j]を選ぶ場合 (ただし1<=j<=k)
    # dp[0][0][0] = 1 #初期値(シード的な)
    # dp = 0 # 上記以外の場合
    dp[0][0][0] = 1
    for s in range(len(dp[0][0])):
        for k in range(len(dp[0])):
            for j in range(len(dp)):
                if j > 0: # 解説では j > 0 and x[j] >= sらしい
                    dp[j][k][s] += dp[j-1][k][s]
                    if j > 0 and k > 0 and s >= x[j]:
                        dp[j][k][s] += dp[j-1][k-1][s-x[j]]
                print("dp[{}][{}][{}]:{}".format(j, k, s, dp[j][k][s]))
    for k in range(len(dp[1])):
        for j in range(len(dp[0])):
            print(dp[j][k])
    count = 0
    for k in range(len(dp[0])):
        print("dp[{}][{}][{}]:{}".format(n-1, k, a*k, dp[n-1][k][a*k]))
        if k > 0:
            count += dp[n-1][k][a*k]
    return count

# n, a = [int(i) for i in input().split()]
# x = [int(i) for i in input().split()]
# x.sort()
print(func(4, 8, [7, 8, 9, 9]))