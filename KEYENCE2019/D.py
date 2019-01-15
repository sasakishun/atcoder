def func(n, m, a, b):
    # i以下の数字なら入れられるマスの数
    under = [0 for _ in range(n * m)]
    fixed = [False for _ in range(n * m)]
    for i in range(n):
        for j in range(m):
            if a[i] == b[j]:
                if fixed[a[i]]:
                    print(0)
                    exit()
                fixed[a[i]] = True
            else:
                under[min(a[i], b[j])] += 1
    # print("und:{}".format(under))
    # _fixed = [0 for i in range(len(fixed))]
    # for i in range(len(_fixed)):
        # if fixed[i]:
            # _fixed[i] = 1
    # print("fix:{}".format(_fixed))
    count = 1
    margin = 0
    for i in reversed(range(len(under))):
        margin += under[i]
        if fixed[i]:
            continue
        else:
            count *= margin
            count %= (10**9) + 7
            margin -= 1
    count %= (10 ** 9) + 7
    # print("count:{}".format(count))
    return count


n, m = [int(i) for i in input().split()]
a = [int(i) - 1 for i in input().split()]
b = [int(i) - 1 for i in input().split()]
# print("func({}, {}, {}, {})".format(n, m, a, b))
# exit()
print(func(n, m, a, b))

"""
print("{} (2)\n".format(2 == func(2, 2, [3, 2], [2, 3])))
print("{} (0)\n".format(0 == func(3, 3, [4, 8, 6], [2, 5, 8])))

print("{}\n{}\n".format(
    343772227, func(14, 13, [157, 166, 180, 146, 177, 150, 178, 181, 175, 168, 179, 128, 174, 167],
                      [180, 149, 177, 178, 166, 179, 175, 168, 181, 176, 174, 158, 172])))
# print("{} (2)\n".format(2 == func(3, 3, [8, 7, 6], [8, 5, 2])))
"""
