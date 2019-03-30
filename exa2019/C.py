n, Q = [int(i) for i in input().split()]
s = input()
q = []
for i in range(Q):
    t, d = [i for i in input().split()]
    q.append([t, d])

last = len(s)
right = ["0", 0, len(s)]
next = [s[-1], 0, 0] # "L, R"
left = ["0", 0, -1]
lNext = [s[0], 0, 0] # "L, R"
for i in reversed(range(Q)):
    print("{} next:{} right:{}".format(i, next, right))
    if q[i][0] == next[0]:
        if q[i][1] == "R":
            next[2] += 1
        else:
            next[1] += 1
    if q[i][0] == right[0] and q[i][1] == "L":
        right[1] += 1
    if next[2] > right[1]:
        if right[2] == 0:
            right[2] -= 1
            break
        right = [next[0], 0, right[2]-1]
        next = [s[right[2]-1], 0, 0]
last =
for i in reversed(range(Q)):
    print("{} lNext:{} left:{}".format(i, lNext, left))
    # 左で消滅する場合
    if q[i][0] == lNext[0]:
        if q[i][1] == "R":
            lNext[2] += 1
        else:
            lNext[1] += 1
    if q[i][0] == left[0] and q[i][1] == "R":
        left[2] += 1
    if lNext[1] > left[1]:
        if left[2] == len(s)-1:
            left[2] += 1
            break
        left = [lNext[0], 0, left[2]+1]
        lNext = [s[left[2]+1], 0, 0]
