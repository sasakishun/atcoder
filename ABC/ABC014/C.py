n = int(input())
imos = [0 for _ in range(10**6 + 2)]
for i in range(n):
    a, b = [int(i) for i in input().split()]
    imos[a] += 1
    imos[b+1] -= 1
# print(sum(imos))
maxCount = imos[0]
for i in range(1, len(imos)):
    imos[i] += imos[i-1]
    maxCount = max(maxCount, imos[i])
print(maxCount)
# print(sum(imos))