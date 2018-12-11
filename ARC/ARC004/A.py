import math

n = int(input())
point = [[0, 0] for _ in range(n)]

for i in range(len(point)):
    point[i] = [int(i) for i in input().split()]
maxDis = 0
for i in range(len(point) - 1):
    for j in range(len(point)):
        maxDis = max(maxDis,
                     (point[i][0]-point[j][0])**2
                     + (point[i][1]-point[j][1])**2)
print(math.sqrt(maxDis))