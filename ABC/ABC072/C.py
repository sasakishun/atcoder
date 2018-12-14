n = int(input())
a = [int(i) for i in input().split()]
table = [0 for i in range(10**5+2)]#末尾は番兵
for i in range(len(a)):
    table[a[i]] += 1
    if a[i] > 0:
        table[a[i]-1] += 1
    table[a[i] + 1] += 1
maxCount = 0
for i in range(len(table)-1):
    maxCount = max(maxCount, table[i])
print(maxCount)