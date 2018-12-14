n = int(input())
x = [0 for i in range(n)]
y = [0 for i in range(n)]
h = [0 for i in range(n)]
height_tmp = 0
X = 0
Y = 0
for i in range(n):
    x[i], y[i], h[i] = [int(i) for i in input().split()]
    if h[i] != 0:
        height_tmp = h[i]
        X = x[i]
        Y = y[i]
for i in range(101):
    for j in range(101):
        flag = 0
        okFlag = 1
        H = height_tmp + abs(X - i) + abs(Y - j)
        if H < 0:
            continue
        for k in range(n):
            if h[k] != max(H - abs(x[k] - i) - abs(y[k] - j), 0):
                okFlag = 0
                break
        if okFlag == 1:
            print("{} {} {}".format(i, j, H))
            exit()
"""
        flag = 0
        okFlag = 1
        height_tmp = 0
        output = [0, 0, 0]
        for k in range(n):
            if h[k] == 0:
                continue
            if flag == 0:
                height_tmp = h[k] + abs(x[k] - i) + abs(y[k] - j)
                flag = 1
            else:
                if height_tmp != h[k] + abs(x[k]-i) + abs(y[k]-j):
                    okFlag = 0
                    break
                elif k == n-1:
                    if height_tmp == h[k] + abs(x[k] - i) + abs(y[k] - j):
                        output = [i, j, height_tmp]
                        okFlag = 1
                        #print("{} {} {}".format(i, j, height_tmp))
                        #exit()
        if okFlag == 1:
            print("{} {} {}".format(i, j, height_tmp))
            exit()
"""
