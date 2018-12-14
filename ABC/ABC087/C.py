n = int(input())
a1 = [int(i) for i in input().split()]
a2 = [int(i) for i in input().split()]

maxSum = 0
for i in range(n):
    sum = 0
    for j in range(i+1):
        sum += a1[j]
    for j in range(i, n):
        sum += a2[j]
    maxSum = max(maxSum, sum)
print(maxSum)