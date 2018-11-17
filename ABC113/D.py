h, w, k = [int(i) for i in input().split()]
h += 1
if w == 1:
    print(1)
    exit()
edge = [0 for i in range(w)]
edge[0] = 1
edge[1] = 2
for i in range(2, w):
    edge[i] = edge[i - 1] + edge[i - 2]
# print("edge:{}".format(edge))

dp = [[0 for j in range(w)] for i in range(h)]
dp[0][0] = 1
dp[0][1] = 0
for i in range(h - 1):
    for j in range(w):
        add = 1
        if 0 <= j - 1 < w:  # 小さい側
            add *= edge[j - 1]
            # print(add)
        if 0 <= w - j - 2 < w:  # 大きい側
            add *= edge[w - j - 2]
            # print(add)
        dp[i + 1][j] += dp[i][j] * add
        # print("h:{} j:{} j:{}".format(i, j, add))
        if j - 1 >= 0:
            add = 1
            if 0 <= j - 2 < w:
                add *= edge[j - 2]
            if 0 <= w - j - 2 < w:
                add *= edge[w - j - 2]
            dp[i + 1][j - 1] += dp[i][j] * add
            # print("h:{} j:{} j-1:{}".format(i, j, add))
        if j + 1 < w:
            add = 1
            if 0 <= j - 1 < w:
                add *= edge[j - 1]
            if 0 <= w - j - 3 < w:
                add *= edge[w - j - 3]
            dp[i + 1][j + 1] += dp[i][j] * add
            # print("h:{} j:{} j+1:{}".format(i, j, add))
        # for i in range(h):
        # print(dp[i])
print(dp[-1][k - 1] % 1000000007)
