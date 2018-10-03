k = 3  # int(input())
r = [2000, 2500, 2300, 2700, 2100, 2400, 2600, 2200]
# [0 for i in range(k)]
DP = [[0 for i in range(2 ** i)] for i in range(k + 1)]
#for i in range(k):
    #r[i] = int(input())

def printDP():
    for i in range(len(DP)):
        print(DP[i])

printDP()
