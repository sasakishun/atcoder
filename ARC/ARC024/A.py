L, R = [int(i) for i in input().split()]
l = [int(i) for i in input().split()]
r = [int(i) for i in input().split()]
l = sorted(l)
r = sorted(r)
# print("r:{}".format(r))
# print("l:{}".format(l))
count = 0
lCounter = 0
rCounter = 0
while lCounter < L and rCounter < R:
    while rCounter < R and r[rCounter] < l[lCounter]:
        rCounter += 1
    if rCounter < R and r[rCounter] == l[lCounter]:
        count += 1
        # print("r[{}]:{} l[{}]:{}".format(rCounter, r[rCounter], lCounter, l[lCounter]))
        rCounter += 1
    lCounter += 1
print(count)