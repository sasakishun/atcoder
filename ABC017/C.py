n, m = [int(i) for i in input().split()]
l = [0 for _ in range(n)]
r = [0 for _ in range(n)]
s = [0 for _ in range(n)]
for i in range(n):
    l[i], r[i], s[i] = [int(i) for i in input().split()]
    l[i] -= 1
    r[i] -= 1


# 1つ以上取得しない宝石がある場合を考える(O(n))
imos = [0 for i in range(m+1)]
selected = [[] for i in range(len(imos))]
for i in range(n):
    imos[l[i]] += s[i]
    imos[r[i] + 1] -= s[i]
for i in range(1, len(imos)):
    imos[i] += imos[i-1]
# print(imos)
totalScore = 0
minScore = imos[0]
for i in range(n):
    totalScore += s[i]
for i in range(1, m):
    minScore = min(minScore, imos[i])
print(totalScore - minScore)