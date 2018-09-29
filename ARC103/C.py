n = int(input())
v = [int(i) for i in input().split()]

numList = [[0, i] for i in range(10**5+1)]
numList2 = [[0, i] for i in range(10**5+1)]

for i in range(n):
    if i % 2 == 1:
        numList[v[i]][0] += 1
    else:
        numList2[v[i]][0] += 1

numList = list(reversed(sorted(numList)))
numList2 = list(reversed(sorted(numList2)))

if numList[0][1] == numList2[0][1]:
    print(n - max(numList[0][0] + numList2[1][0],numList[1][0] + numList2[0][0]))
else:
    print(n - numList[0][0] - numList2[0][0])
