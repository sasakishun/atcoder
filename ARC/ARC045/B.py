def show(a):
    for i in range(len(a)):
        print(a[i])
    print()


def func(n, m, a):
    # つまりは全[s, t]区間において、
    # 完全に重複している区間を選べということ
    table = [0 for _ in range(n + 2)]
    # imos法で,各部屋の重複数を調べる
    for i in range(m):
        table[a[i][0]] += 1
        table[a[i][1] + 1] -= 1
    for i in range(1, len(table)):
        table[i] += table[i - 1]

    # 重複していない、つまり1の箇所のみを考えればよい
    # ここでは1以外のマスは0にして、
    # 累積後は自身より前の値と同じにする
    for i in range(1, len(table)):
        if table[i] != 1:
            table[i] = 0
        table[i] += table[i - 1]
    # print(table)
    # このように再びimos法で累積和をとると
    # 1のマスを含むと,累積和が増える、
    # つまり重複がないマスを含む区間では、
    # table[x] != table[y]となる
    # よって調べる区間で
    # 「table[x] == table[y]」かどうかを調べればよい
    out = []
    for i in range(m):
        if table[a[i][0] - 1] == table[a[i][1]]:
            out.append(i)
    print(len(out))
    for i in range(len(out)):
        print(out[i] + 1)


n, m = [int(i) for i in input().split()]
a = [[0, 0, 0] for _ in range(m)]
for i in range(m):
    a[i] = [int(i) for i in input().split()]
# func(10, 5, [[1, 4], [5, 5], [6, 8], [9, 10], [5, 6]])
func(n, m, a)
