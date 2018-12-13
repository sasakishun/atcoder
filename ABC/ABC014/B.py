n, x = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]

# output = []
_sum = 0
for j in range(len(a)):
    if ((x >> j) & 1) == 1:
        _sum += a[j]
        # output.append(j)  # このjが今回探索するindexの1つ
print(_sum)
"""
N = [i for i in range(10)]  # N = bit探索する桁数
# Nの要素の全組み合わせが出力
for i in range(1, 1 << len(N)):
    output = []
    for j in range(len(N)):
        if ((i >> j) & 1) == 1:
            output.append(j)  # このjが今回探索するindexの1つ
    print(output)
"""
