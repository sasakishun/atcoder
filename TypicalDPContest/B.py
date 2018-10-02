import math

A, B = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
a.append(0)
b.append(0)
a.append(0)
b.append(0)
DP = [[0 for i in range(B + 2)] for j in range(A + 2)]

maxScore = 0
"""
def search(lastA, lastB, score):
    # print("A:{} B:{} score:{}".format(lastA, lastB, score))
    if lastA == A and lastB == B:
        global maxScore
        maxScore = max(maxScore, score)
        return score
    elif DP[lastA][lastB] != -math.inf:
        return score
    else:
        if lastA == A:
            score = search(lastA, lastB + 1, score + b[lastB] * ((lastA + lastB + 1) % 2))
        elif lastB == B:
            score = search(lastA + 1, lastB, score + a[lastA] * ((lastA + lastB + 1) % 2))
        else:
            if (lastA + lastB) % 2 == 0:
                score = max(search(lastA + 1, lastB, score + a[lastA] * ((lastA + lastB + 1) % 2)),
                            search(lastA, lastB + 1, score + b[lastB] * ((lastA + lastB + 1) % 2)))
            else:
                score = min(search(lastA + 1, lastB, score),
                            search(lastA, lastB + 1, score))
        DP[lastA][lastB] = score
        # print(DP)
        return score


search(0, 0, 0)
# for i in range(len(DP)):
# print(DP[i])
print(maxScore)
"""
for i in reversed(range(A+1)):
    for j in reversed(range(B+1)):
        # print("{}:{}".format(i, j))
        if i == A:
            DP[i][j] = DP[i][j + 1] \
                       + b[j] * ((i + j + 1) % 2)
        elif j == B:
            DP[i][j] = DP[i + 1][j] \
                       + a[i] * ((i + j + 1) % 2)
        elif (i + j) % 2 == 0:
            DP[i][j] = \
                max(DP[i + 1][j] + a[i],
                    DP[i][j + 1] + b[j])
        else:
            DP[i][j] = \
                min(DP[i + 1][j],
                    DP[i][j + 1])
#for i in reversed(range(len(DP))):
    #print("{} {}".format(b[i], DP[i]))
#print("  {}".format(a))
print(DP[0][0])