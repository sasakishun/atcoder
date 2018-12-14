n, k = [int(i) for i in input().split()]

divList = [0 for i in range(k)]
for i in range(1, n+1):
    divList[i % k] += 1

# print(divList)

count = 0
for i in range(k):
    if (i*2) % k == 0:
        count += divList[i] ** 3
print(count)