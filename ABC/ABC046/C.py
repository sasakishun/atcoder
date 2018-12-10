import math

n = int(input())
vote = [0, 0]
# 最初の得票は、最小値を目指すので
# 単純に入力比をそのまま使用
# 各入力に対し、vote[0]<tk, vote[1]<akとなる
# 最小のtk,akでvoteを更新
for i in range(n):
    t, a = [int(i) for i in input().split()]
    if i == 0:
        vote = [t, a]
        continue
    k = max(int(vote[0] / t),
            int(vote[1] / a))
    if t*k < vote[0] or a*k < vote[1]:
        # print("miss")
        k = max(math.ceil(vote[0] / t),
                math.ceil(vote[1] / a))
    vote = [t * k, a * k]
    # print("[{},{}] k:{}".format(t, a, k))
    # print("vote:{}".format(vote))
print(vote[0] + vote[1])
