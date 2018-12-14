n = int(input())
t = [0 for _ in range(n)]
for i in range(n):
    t[i] = int(input())
t = sorted(t)
time = 10**5
# n<4なので,ビット全探索
N = [i for i in range(n)]  # N = bit探索する桁数
# Nの要素の全組み合わせが出力
for i in range(1, 1 << len(N)):
    output = []
    a = 0
    b = 0
    for j in range(len(N)):
        if ((i >> j) & 1) == 1:
            output.append(j)  # このjが今回探索するindexの1つ
            a += t[j]
        else:
            b += t[j]
    time = min(time, max(a, b))
    # print(output)
print(time)

