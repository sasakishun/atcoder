import heapq


class dijkstra:
    def __init__(self, adj):
        self.adj = adj
        self.visited = [-1 for i in range(len(adj))]
        self.heap = []

    def allSearch(self, _start):
        # スタート地点を設定
        heapq.heappush(self.heap, [0, _start])
        # ダイクストラ法でスタート地点からの距離を算出
        while 1:
            if len(self.heap) == 0:
                break
            start = heapq.heappop(self.heap)
            # 同じノードへ複数候補がある場合がある、一度訪れたノードへの候補は削除する
            if self.visited[start[1]] != -1:
                continue
            # 確定した距離をvisitテーブルに保持
            self.visited[start[1]] = start[0]
            for i in range(len(self.adj)):
                if self.visited[i] == -1 and self.adj[start[1]][i] != 0:
                    heapq.heappush(self.heap, [self.adj[start[1]][i] + self.visited[start[1]], i])
        # print("start:{} score:{}".format(_start, max(self.visited)))
        return self.visited


class binarySearch():
    # 入力tableはソートされていることが前提
    def __init__(self, limit, adj):
        self.limit = limit
        self.adj = adj
        # print("table:{}".format(table))

    # min(table) <= target <= max(table)が前提
    def search(self, target):
        low = 0
        high = self.limit
        # t は中央番目の数
        t = int((low + high) / 2)
        target = -1
        # print("low:{} high:{}".format(low, high))
        # 探索の下限のlowが上限のhighになるまで探索
        # lowがhighに達すると数は見つからなかったということ
        while high >= low:
            for i in range(len(_adj)):
                for j in range(len(_adj[i])):
                    # print("i:{} j:{}".format(i, j))
                    if _adj[i][j] == "#":
                        # 自身が"#"なら行き先からの重みを1にする
                        if i + 1 < h:
                            adj[w * (i + 1) + j][w * i + j] = t
                        if j + 1 < w:
                            adj[w * i + j + 1][w * i + j] = t
                    else:
                        if i + 1 < h:
                            adj[w * (i + 1) + j][w * i + j] = 1
                        if j + 1 < w:
                            adj[w * i + j + 1][w * i + j] = 1
                    if i + 1 < h:
                        if _adj[i + 1][j] == "#":
                            adj[w * i + j][w * (i + 1) + j] = t
                        else:
                            adj[w * i + j][w * (i + 1) + j] = 1
                    if j + 1 < w:
                        if _adj[i][j + 1] == "#":
                            adj[w * i + j][w * i + j + 1] = t
                        else:
                            adj[w * i + j][w * i + j + 1] = 1
            # print()
            # for i in adj:
                # print(i)
            dij = dijkstra(adj=adj)
            _target = dij.allSearch(start)[goal]
            # print("t:{} cost:{} limit:{}".format(t, _target, _t))
            if target == _target:
                break
            else:
                target = _target
            if target < _t:
                # targetが上に
                low = t + 1
            elif target > _t:
                high = t - 1
            t = int((low + high) / 2)
        return t

h, w, _t = [int(i) for i in input().split()]
_adj = [[0 for i in range(w)] for j in range(h)]
# _adj = [['S', '#', '#'], ['.', '#', 'G']]
adj = [[0 for i in range(w * h)] for j in range(w * h)]
start = 0
goal = 5  # 0
cost = 0
out = 0
for i in range(h):
    _inpAdj = input()
    for j in range(w):
        _adj[i][j] = _inpAdj[j]
        if _inpAdj[j] == "S":
            start = w * i + j
        if _inpAdj[j] == "G":
            goal = w * i + j
# print(_adj)
# 要するに隣接行列を拡張する
# "#"に繋がる辺は重みt,それ以外は1とする
binary = binarySearch(_t, _adj)
print(binary.search(_t))
