class UnionFind():
    # 負の値はルートで集合の個数
    # 正の値は次の要素を返す
    def __init__(self, size):
        self.table = [-1 for _ in range(size)]

    # 集合の代表を求める
    def find(self, x):
        while self.table[x] >= 0:
            # 根に来た時,self.table[根のindex]は負の値なのでx = 根のindexで値が返される。
            x = self.table[x]
        return x

    # 併合
    def union(self, x, y):
        s1 = self.find(x)  # 根のindex,table[s1]がグラフの高さ
        s2 = self.find(y)
        if s1 != s2:  # 根が異なる場合
            if self.table[s1] != self.table[s2]:  # グラフの高さが異なる場合
                if self.table[s1] < self.table[s2]:
                    self.table[s2] = s1
                else:
                    self.table[s1] = s2
            else:
                # グラフの長さが同じ場合,どちらを根にしても変わらない
                # その際,グラフが1長くなることを考慮する
                self.table[s1] += -1
                self.table[s2] = s1
        return


h, w = [int(i) for i in input().split()]
s = [[0 for _ in range(w)] for _ in range(h)]
for i in range(h):
    s[i] = list(input())

union = UnionFind(h * w)

for i in range(h):
    for j in range(w):
        if i > 0 and s[i][j] != s[i - 1][j]:
            union.union(w * i + j, w * (i - 1) + j)
        if j > 0 and s[i][j] != s[i][j - 1]:
            union.union(w * i + j, w * i + (j - 1))
out = [[0, 0] for _ in range(h * w)]
for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            out[union.find(w * i + j)][0] += 1
        else:
            out[union.find(w * i + j)][1] += 1
count = 0
for _out in out:
    count += _out[0] * _out[1]
print(count)