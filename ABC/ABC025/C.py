import copy
b = [[0 for i in range(3)] for j in range(2)]
c = [[0 for i in range(2)] for j in range(3)]

def getScore(state):
    score = [0, 0]
    for i in range(2):
        for j in range(3):
            if state[i][j] == state[i + 1][j]:
                score[state[i][j]] += b[i][j]
    for i in range(3):
        for j in range(2):
            if state[i][j] == state[i][j + 1]:
                score[state[i][j]] += c[i][j]
    # print("score:{}".format(score))
    return score
# 状況stateにおいてplayerが最善手を取った場合のスコアを返す
def search(_state, player, lastTurn):
    state = copy.deepcopy(_state)
    # print(lastTurn)
    if lastTurn == 0:
        return getScore(state)
    else:
        score = [0, 0]
        for i in range(3):
            for j in range(3):
                if state[i][j] == -1:
                    if player == 0:
                        tmpState = copy.deepcopy(state)
                        tmpState[i][j] = 0
                        score[0] = \
                            max(score[0], search(tmpState, (player + 1) % 2, lastTurn - 1)[0])
                    if player == 1:
                        tmpState = copy.deepcopy(state)
                        tmpState[i][j] = 1
                        score[1] = \
                            max(score[1], search(tmpState, (player + 1) % 2, lastTurn - 1)[1])
        return score

for i in range(2):
    b[i] = [int(i) for i in input().split()]
for i in range(3):
    c[i] = [int(i) for i in input().split()]
print(search([[-1 for j in range(3)] for i in range(3)], 0, 9))
