a, b, c = [int(i) for i in input().split()]

count = 0
while True:
    if a % 2 != 0 or b % 2 != 0 or c % 2 != 0:
        print(count)
        exit()
    if a == b == c:
        print("-1")
        exit()
    _a = a
    _b = b
    _c = c
    a = int(_b / 2 + _c / 2)
    b = int(_c / 2 + _a / 2)
    c = int(_b / 2 + _c / 2)
    count += 1
    # print("a:{} b:{} c:{} count:{}".format(a, b, c, count))
