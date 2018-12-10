n, k = [int(i) for i in input().split()]
t = [[0 for _ in range(k)] for _ in range(n)]
for i in range(n):
    t[i] = [int(i) for i in input().split()]


# n,k共に小さいので全探索でOK
def search(questionNum, score):
    # print(questionNum)
    if questionNum == n:
        # print("score:{}".format(score))
        return score
    for i in range(len(t[questionNum])):
        # print("xor:{}".format(score ^ t[questionNum][i]))
        score = search(questionNum+1, int(score ^ t[questionNum][i]))
        if score == 0:
            return 0
    return score

for i in range(len(t[0])):
    if search(1, t[0][i]) == 0:
        print("Found")
        exit()
print("Nothing")