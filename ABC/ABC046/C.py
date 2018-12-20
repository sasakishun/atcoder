import math

n = int(input())
vote = [0, 0]
# 最初の得票は、最小値を目指すので
# 単純に入力比をそのまま使用
# 各入力に対し、vote[0]<=t*k, vote[1]<=a*kとなる
# 最小のt*k,a*kでvoteを更新
vote = [1, 1]
for i in range(n):
    t, a = [int(i) for i in input().split()]
    if vote[0] % t == 0:
        k = vote[0] // t
    else:
        k = vote[0] // t + 1
    if vote[1] % a == 0:
        k = max(k, vote[1] // a)
    else:
        k = max(k, vote[1] // a + 1)
    # k = max(math.ceil(vote[0] / t), math.ceil(vote[1] / a))
    vote = [t * k, a * k]
    # a / b + (a % b == 0 ? 0: 1)
    # print("i:{} vote:{}".format(i, vote))
print(vote[0] + vote[1])
