import heapq


class dijkstra:
    def __init__(self, adj):
        self.adj = adj
        self.visited = [-1 for _ in range(len(adj))]
        self.heap = []

    def allSearch(self, _start):
        heapq.heappush(self.heap, [0, _start])
        while 1:
            if len(self.heap) == 0:
                break
            start = heapq.heappop(self.heap)
            # 同じノードへ複数候補がある場合がある、
            # 一度訪れたノードへの候補は削除する
            if self.visited[start[1]] != -1:
                continue
            # 確定した距離をvisitテーブルに保持
            self.visited[start[1]] = start[0]
            for i in range(len(self.adj)):
                if -self.adj[start[1]][i] - self.visited[start[1]] < -self.visited[i]:
                    heapq.heappush(self.heap, [-(self.adj[start[1]][i] + self.visited[start[1]]), i])
                if self.visited[i] == -1 and self.adj[start[1]][i] != 0:
                    heapq.heappush(self.heap,
                                   [-(self.adj[start[1]][i] + self.visited[start[1]]),
                                    i,
                                    self.adj[start[1]][i] + self.visited[start[1]]])
        # print("start:{} score:{}".format(_start, max(self.visited)))
        return self.visited


_min = -10 ** 12
n, m = [int(i) for i in input().split()]
adj = [[_min for _ in range(n)] for _ in range(n)]
for _ in range(m):
    a, b, c = [int(i) for i in input().split()]
    adj[a - 1][b - 1] = c
dij = dijkstra(adj)
dij.allSearch(0)
print(dij.visited[0][-1])
