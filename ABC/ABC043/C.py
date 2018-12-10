n = int(input())
a = [int(i) for i in input().split()]

minCost = 10000*1000
for i in range(101):
    cost = 0
    for j in range(len(a)):
        cost += (i - a[j])**2
    if cost < minCost:
        minCost = cost
    cost = 0
    for j in range(len(a)):
        cost += (i + a[j]) ** 2
    if cost < minCost:
        minCost = cost
print(minCost)