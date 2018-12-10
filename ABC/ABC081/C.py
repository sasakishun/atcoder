n, k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
a = sorted(a)
a.append(-1)
variation = []
target = a[0]
start = 0
for i in range(len(a)):
    if a[i] != target:
        variation.append(i-start)
        start = i
        target = a[i]
variation = sorted(variation)
cost = 0
for i in range(len(variation) - k):
    cost += variation[i]
print(cost)