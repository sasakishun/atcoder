def func(x1, y1, x2, y2):
    x3 = x2 - (y2 - y1)
    y3 = y2 + (x2-x1)
    return x3, y3

x1, y1, x2, y2 = [int(i) for i in input().split()]
x3, y3 = func(x1, y1, x2, y2)
x4, y4 = func(x2, y2, x3, y3)
print("{} {} {} {}".format(x3, y3, x4, y4))
"""
if x1 == x2 and y1 < y2:
    hen = y2 - y1
    print("{} {} {} {}".format(x1-hen, y2, x1-hen, y1))
elif x1 > x2 and y1 == y2:
    hen = x1 - x2
    print("{} {} {} {}".format(x2, y2-hen, x1, y1-hen))
elif x1 == x2 and y1 > y2:
    hen = y1 - y2
    print("{} {} {} {}".format(x2+hen, y2, x2+hen, y1))
elif x1 < x2 and y1 == y2:
    hen = x2 - x1
    print("{} {} {} {}".format(x2, y2+hen, x1, y1+hen))
    """