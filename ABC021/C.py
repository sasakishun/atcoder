import heapq


class dijkstra:
    def __init__(self, adj):
        self.adj = adj
        self.visited = [-1 for i in range(len(adj))]
        self.counter = [0 for i in range(len(adj))]
        self.heap = []

    def showAdj(self):
        print("adj matrix")
        for i in range(len(self.adj)):
            print(adj[i])

    def allSearch(self, _start):
        # スタート地点を設定
        # [目標頂点への総距離, 目標頂点, 出発頂点]
        heapq.heappush(self.heap, [0, _start, 0])
        # ダイクストラ法でスタート地点からの距離を算出
        while 1:
            if len(self.heap) == 0:
                break
            start = heapq.heappop(self.heap)
            # 一度訪れたノードへの候補は削除する
            # if self.visited[start[1]] != -1:
            # continue

            # 確定した距離をvisitテーブルに保持
            # self.visited[start[1]] = start[0]
            # 今回の特別処理
            # self.showAdj()
            # print(start[1])
            if self.visited[start[1]] == -1 or \
                            self.visited[start[1]] > start[0]:
                self.counter[start[1]] = 1
                self.visited[start[1]] = start[0]
            elif self.visited[start[1]] == start[0]:
                self.counter[start[1]] += 1
            adj[start[1]][start[2]] = 0
            adj[start[2]][start[1]] = 0
            for i in range(len(self.adj)):
                # if self.visited[i] == -1 and self.adj[start[1]][i] != 0:
                if self.adj[start[1]][i] != 0:
                    heapq.heappush(self.heap, [self.adj[start[1]][i] + self.visited[start[1]], i, start[1]])
        # print("start:{} score:{}".format(_start, max(self.visited)))
        return self.visited


n = int(input())
a, b = [int(i) - 1 for i in input().split()]
m = int(input())
adj = [[0 for i in range(n)] for j in range(n)]
for i in range(m):
    x, y = [int(i) - 1 for i in input().split()]
    adj[x][y] = 1
    adj[y][x] = 1
# 通常のdijkstraのように探索した地点をvisitedとするのではなく
# 探索した辺を削除していけばよい
# そして各頂点への距離を算出する際に、距離が同じなら
# その頂点への最短経路数をインクリメントし
# そうでないなら、その頂点への最短経路を更新する
minDist = 100000
dij = dijkstra(adj=adj)
dij.allSearch(a)
print(dij.counter[b])
