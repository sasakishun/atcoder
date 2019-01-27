n = int(input())
a = [0 for _ in range(n)]
b = [0 for _ in range(n)]
cost = [[0, 0] for _ in range(n)]
for i in range(n):
    a[i], b[i] = [int(i) for i in input().split()]
    cost[i] = [a[i]+b[i], i]
# a[i]-b[i]がmaxのものから取っていく
cost.sort()
cost.reverse()
scoreA = 0
scoreB = 0
for i in range(len(cost)):
    if i % 2 == 0:
        scoreA += a[cost[i][1]]
    else:
        scoreB += b[cost[i][1]]
print(scoreA -scoreB)