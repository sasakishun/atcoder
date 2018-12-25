n, k = [int(i) for i in input().split()]
t = [[0 for _ in range(k)] for _ in range(n)]
for i in range(n):
    t[i] = [int(i) for i in input().split()]


# n,k共に小さいので全探索でOK
def search(questionNum, score):
    # print(questionNum)
    if questionNum == n:
        if score == 0:
            print("Found")
            exit()
        # print("score:{}".format(score))
        return
    for i in t[questionNum]:
        # print("xor:{}".format(score ^ t[questionNum][i]))
        search(questionNum+1, score ^ i)
    return

for i in range(len(t[0])):
    search(1, t[0][i])
print("Nothing")
