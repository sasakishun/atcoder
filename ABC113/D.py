h, w, k = [int(i) for i in input().split()]

dp = [[1 for j in range(w)] for i in range(h)]
for i in range(1, h):
    for j in range(w):
        dp[i+1][j] = dp[i][j]*((w-3)**2)
        dp[i+1][j-1] = dp[i][j]*2
        dp[i+1][j+1] = dp[i][j]*2