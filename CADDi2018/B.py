import copy

# 最後のリンゴを食べたものが勝者
"""
def func(_left, turn):
    left = []
    for i in _left:
        if i != 0:
            left.append(i)
    N = [i for i in range(len(left))]  # N = bit探索する桁数
    # Nの要素の全組み合わせが出力
    winFlag = False
    for i in range(1, 1 << len(N)):
        output = []
        copyLeft = copy.deepcopy(left)
        minus = 0
        for j in range(len(N)):
            if ((i >> j) & 1) == 1:
                output.append(j)  # このjが今回探索するindexの1つ
                if copyLeft[j] > 0:
                    copyLeft[j] -= 1
                    minus += 1
        if minus == 0:
            continue
        # if sum(copyLeft) == 0:
            # print("winner:{}({}) select:{}".format(turn, (turn+1) % 2, output))
        if func(copyLeft, turn + 1):
            winFlag = True
    return not winFlag

def answer(a, turn):
    if not func(a, turn):
        return "{}:1st".format(a)
    else:
        return "{}:2nd".format(a)
print(answer([1], 0))
print(answer([2], 0))
print(answer([3], 0))
print(answer([4], 0))
print(answer([5], 0))
print(answer([6], 0))

print(answer([1, 1], 0))
print(answer([2, 1], 0))
print(answer([2, 2], 0))
print(answer([3, 1], 0))
print(answer([3, 2], 0))
print(answer([3, 3], 0))
print(answer([4, 2], 0))
print(answer([4, 4], 0))

print(answer([1, 1, 1], 0))
print(answer([2, 1, 1], 0))
print(answer([2, 2, 1], 0))
print(answer([2, 2, 2], 0))

print(answer([1, 1, 1], 0))
print(answer([2, 1, 1], 0))
print(answer([2, 2, 1], 0))
print(answer([2, 2, 2], 0))
print(answer([3, 1, 1], 0))
print(answer([3, 2, 1], 0))
print(answer([3, 2, 2], 0))
print(answer([3, 3, 1], 0))
print(answer([3, 3, 2], 0))
print(answer([3, 3, 3], 0))
print(answer([4, 4, 4], 0))
"""
"""
print()
print(answer([4, 1, 1, 1], 0))
print(answer([4, 2, 1, 1], 0))
print(answer([4, 2, 2, 1], 0))
print(answer([4, 2, 2, 2], 0))
print(answer([4, 1, 1, 1], 0))
print(answer([4, 1, 1, 1], 0))
print(answer([4, 1, 1, 1], 0))
print(answer([4, 1, 1, 1], 0))
"""
n = int(input())
a = [0 for _ in range(n)]
for i in range(n):
    a[i] = int(input())
for _a in a:
    if _a % 2 == 1:
        print("first")
        exit()
print("second")