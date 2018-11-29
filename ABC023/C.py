R, C, k = [int(i) for i in input().split()]
n = int(input())
a = [[0 for i in range(C)] for i in range(R)]
r = [[0, i] for i in range(R)]
c = [[0, i] for i in range(C)]

for i in range(n):
    _r, _c = [int(i) - 1 for i in input().split()]
    r[_r][0] += 1
    c[_c][0] += 1
    a[_r][_c] = 1
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
