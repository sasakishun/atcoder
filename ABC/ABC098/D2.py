def evaluate(digit):
    _digit = str(format(digit, "b"))
    print(_digit)
    for i in range(len(_digit)):
        if int(_digit[i]) > 1:
            return False
    return True

def func(n, a):
    digit = 0
    count = 0
    i = 0
    j = 0
    while j < n:
        while j < n:
            if digit ^ a[j] == digit + a[j]:
                digit += a[j]
                count += j - i + 1
                # print("j i:{} j:{} count:{} digit:{}".format(i, j, count, format(digit, "b")))
                j += 1
            else:
                break
        while i < j < n:
            digit ^= a[i]
            i += 1
            break
        # print("_ i:{} j:{} count:{} digit:{}".format(i, j, count, format(digit, "b")))
    return count
"""
print(func(4, [2, 5, 4, 6]))
print(func(9, [0, 0, 0, 0, 0, 0, 0, 0, 0]))
print(func(19,[885, 8, 1, 128, 83, 32, 256, 206, 639, 16, 4, 128, 689, 32, 8, 64, 885, 969, 1]))
"""
digit = 0
n = int(input())
a = [int(i) for i in input().split()]
print(func(n, a))
