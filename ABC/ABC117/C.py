# nコマ, m地点
def func(n, m, x):
    x.sort()
    dis = []
    for i in range(1, len(x)):
        dis.append(x[i] - x[i-1])
    dis.sort()
    n = min(n, m)
    # print("n:{} dis:{}".format(n, dis))
    print(sum(dis[:m-n]))
# for i in range(1, 10):
    # func(i, 7, [-10, -3, 0, 9, -100, 2, 17])
"""
func(3, 5, [1, 2, 10, 12, 14])
func(3, 7, [-10, -3, 0, 9, -100, 2, 17])
func(100, 1, [-100])
"""
n, m = [int(i) for i in input().split()]
x = [int(i) for i in input().split()]
func(n, m, x)