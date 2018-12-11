y = int(input())
m = int(input())
d = int(input())


def count(y, m, d):
    if m == 1 or m == 2:
        y -= 1
        m += 12
    return 365 * y + int(y / 4) \
           - int(y / 100) + int(y / 400) \
           + int((306 * (m + 1)) / 10) + d - 429


# y年m月d日までの日数は
print(count(2014, 5, 17) - count(y, m, d))