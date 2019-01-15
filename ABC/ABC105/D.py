import math
def cmb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

def func(n, m, a):
    # print("n:{} m:{} a:{}".format(n, m, a))
    for i in range(n):
        if i > 0:
            a[i] += a[i-1]
        a[i] %= m
    a.sort()
    a.append(-1)
    # print(a)
    count = 0
    same = 1
    for i in range(len(a)):
        if a[i] == 0:
            count += 1
        if a[i] == a[i-1]:
            same += 1
        else:
            if same >= 2:
                count += cmb(same, 2)
            same = 1
    return count

n, m = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
print(func(n, m, a))
"""
print(func(3, 2, [4, 1, 5]))
print(func(13, 17, [29, 7, 5, 7, 9, 51, 7, 13, 8, 55, 42, 9, 81]))
print(func(10, 400000000, [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]))
"""
# print("func({}, {}, {})".format(n, m, a))
