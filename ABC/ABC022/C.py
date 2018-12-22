import heapq
import copy


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
                # print("conflicted:{}".format(start[1]))
                # print("visited:{}".format(self.visited))
                continue
            # 確定した距離をvisitテーブルに保持
            self.visited[start[1]] = start[0]
            for i in range(len(self.adj)):
                if self.visited[i] == -1 and self.adj[start[1]][i] != 0:
                    heapq.heappush(self.heap, [self.adj[start[1]][i] + self.visited[start[1]], i])
        # print("start:{} score:{}".format(_start, max(self.visited)))
        return self.visited
    """
    def allSearch(self, _start):
        # スタート地点を設定
        heapq.heappush(self.heap, [-1, _start, -1])
        # [今までの距離, 現在地, 一つ前の場所]

        # heapq.heappush(self.heap, [0, _start])
        # ダイクストラ法でスタート地点からの距離を算出
        while 1:
            if len(self.heap) == 0:
                break
            start = heapq.heappop(self.heap)
            if start[1] != -1 and start[2] != -1:
                # adj[start[1]][start[2]] = 0
                adj[start[2]][start[1]] = 0

            # 同じノードへ複数候補がある場合がある、一度訪れたノードへの候補は削除する
            if self.visited[start[1]] != -1:
                # pushしてから実際にpopされるまでにはラグがあるので
                # その間にvisitされていたら訪問しない
                continue
            # 確定した距離をvisitテーブルに保持
            self.visited[start[1]] = start[0]
            print()
            for i in range(len(adj)):
                print(adj[i])
            for i in range(len(self.adj)):
                if self.visited[i] == -1 and self.adj[start[1]][i] != 0:
                    heapq.heappush(self.heap, [self.adj[start[1]][i] + self.visited[start[1]], i, start[1]])
        # print("start:{} score:{}".format(_start, max(self.visited)))
        return self.visited
    """

minDist = 100000
n, m = [int(i) for i in input().split()]
adj = [[0 for i in range(n)] for j in range(n)]
connectToStart = []
for i in range(m):
    u, v, l = [int(i) for i in input().split()]
    adj[u - 1][v - 1] = l
    adj[v - 1][u - 1] = l
    if u - 1 == 0:
        connectToStart.append(v - 1)
    elif v - 1 == 0:
        connectToStart.append(u - 1)
# print("connect:{}".format(connectToStart))
for i in connectToStart:
    _adj = copy.deepcopy(adj)
    for j in range(len(_adj)):
        if i != j:
            _adj[0][j] = 0
            _adj[j][0] = 0
    # for j in range(len(_adj)):
        # print(_adj[j])
    dij = dijkstra(adj=_adj)
    _visited = dij.allSearch(0)
    for j in connectToStart:
        if i != j:
            minDist = min(minDist, _visited[j]+adj[0][j])
    # print()
    # print(dij.visited)
    # print()
if minDist > 0:
    print(minDist)
else:
    print(-1)
# print()
# for i in range(len(adj)):
    # print(adj[i])
