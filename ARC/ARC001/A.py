n = int(input())
c = input()

score = [0, 0, 0, 0]
for i in range(len(c)):
    score[int(c[i]) - 1] += 1
print("{} {}".format(max(score), min(score)))