n = int(input())
prev = [0, [0, 0]]  # [t, [x, y]]
for i in range(n):
    # print(prev)
    t, x, y = [int(i) for i in input().split()]
    left = (t - prev[0]) - (abs(x - prev[1][0]) + abs(y - prev[1][1]))
    # print("left:{}".format(left))
    if left >= 0 and left % 2 == 0:
        prev = [t, [x, y]]
    else:
        print("No")
        exit()
print("Yes")
