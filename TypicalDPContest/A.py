n = int(input())
p = [int(i) for i in input().split()]

existList = [[0 for i in range(n * 100 + 1)] for j in range(n)]
sumList = [0 for i in range(n * 100 + 1)]


def getScore(local, sum):
    # print("local:{}, sum:{}".format(local, sum))
    if existList[local][sum] != 0:
        return
    if existList[local][sum] == 0:
        existList[local][sum] = 1
        sumList[sum] = 1
    if local < n - 1:
        getScore(local + 1, sum + p[local + 1])
        getScore(local + 1, sum)


# sum(nCm) m=1,2,3,4...
# 得点＝現在の合計+残りn-kつの中の得点

getScore(0, p[0])
getScore(0, 0)
count = 0
for i in range(len(sumList)):
    if sumList[i] != 0:
        #print(i)
        count += 1
print(count)
