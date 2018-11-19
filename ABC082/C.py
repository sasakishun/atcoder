n = int(input())
a = [int(i) for i in input().split()]
a = sorted(a)
a.append(-1)
cost = 0
target = a[0]
start = 0
# print(a)
for i in range(len(a)):
    # print("target:{} start:{} i:{}".format(target, start, i))
    localCost = 1000000
    if a[i] != target:
        if i - start == target:
            localCost = 0
        elif i - start > target:
            localCost = i - start - target
        cost += min(localCost, i - start)
        start = i
        target = a[i]
        # print("local:{} cost:{}".format(min(localCost, i - start), cost))
print(cost)