R, C, k = [int(i) for i in input().split()]
n = int(input())
a = [[0] * C] * R
# r = [[0, i] for i in range(R)]
# c = [[0, i] for i in range(C)]
r = [0] * R
c = [0] * C
candyExist = [[0, 0]] * n
for i in range(n):
    _r, _c = [int(i) - 1 for i in input().split()]
    # r[_r][0] += 1
    # c[_c][0] += 1
    r[_r] += 1
    c[_c] += 1
    a[_r][_c] = 1
    candyExist[i] = [_r, _c]

candyI = [0] * (k + 1)
candyJ = [0] * (k + 1)
for i in range(R):
    if r[i] <= k:
        candyI[r[i]] += 1
for i in range(C):
    if c[i] <= k:
        candyJ[c[i]] += 1
count = 0
candyJ.reverse()
for i in range(k + 1):
    count += candyI.pop() * candyJ.pop()
for i in range(n):
    tmpI, tmpJ = candyExist.pop()
    # print("{} {}".format(tmpI, tmpJ))
    if r[tmpI] + c[tmpJ] == k:
        # 本当の和はk-1となっているので
        count -= 1
    elif r[tmpI] + c[tmpJ] == k + 1:
        # 本当の和はkとなっているので
        count += 1
print(count)

"""
r = sorted(r)
c = sorted(c)
# for i in range(len(a)):
# print(a[i])
count = 0
j = C - 1
for i in range(R):
    # print("j:{}".format(j))
    while r[i][0] + c[j][0] > k + 1:
        # print("a[{}][{}]:{}".format(r[i][1], c[j][1], r[i][0] + c[j][0]))
        j -= 1
    # count += C - j - 1
    # print("add:{} i:{} j:{}".format(C - 1 - j, i, j))
    j2 = j
    while j2 >= 0:
        if r[i][0] + c[j2][0] == k + 1 and a[r[i][1]][c[j2][1]] == 1:
            count += 1
            # print("score==k i:{} j:{}".format(r[i][1], c[j][1]))
        elif r[i][0] + c[j2][0] == k and a[r[i][1]][c[j2][1]] == 0:
            count += 1
            # print("score==k i:{} j:{}".format(r[i][1], c[j][1]))
        j2 -= 1
print(count)
# print(r)
# print(c)
"""
