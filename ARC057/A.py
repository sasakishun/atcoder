a, k = [int(i) for i in input().split()]
if k == 0:
    print(2 * (10 ** 12) - a)
else:
    i = 0
    while a < 2 * (10 ** 12):
        a += 1 + k * a
        i += 1
        # print(a)
    print(i)