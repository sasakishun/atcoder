import copy
import scipy.sparse.csgraph as ssc

# 入力:隣接行列　出力:各頂点間の最短距離
class warshallFloyd:
    def __init__(self, adj):
        # math.infはpython3.5以降のみ使用可能
        self.inf = 10 ** 9
        self.dis = copy.deepcopy(adj)
        for i in range(len(adj)):
            for j in range(len(adj)):
                if i != j and adj[i][j] == 0:
                    self.dis[i][j] = self.inf

    # 全ての頂点間の最短距離を算出、
    def search(self):
        for k in range(len(self.dis)):
            for i in range(len(self.dis)):
                for j in range(len(self.dis)):
                    if self.dis[i][j] > self.dis[i][k] + self.dis[k][j]:
                        self.dis[i][j] = self.dis[i][k] + self.dis[k][j]
        return self.dis

minDist = 10**9
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
_adj = copy.deepcopy(adj)
for j in range(1, len(_adj)):
    _adj[0][j] = 0
    _adj[j][0] = 0

dis = ssc.floyd_warshall(_adj)
# war = warshallFloyd(adj=_adj)
# dis = war.search()
for i in connectToStart:
    for j in connectToStart:
        if i != j:
            minDist = min(minDist, dis[i][j] + adj[0][i] + adj[0][j])
if minDist == 10**9:
    print(-1)
else:
    print(int(minDist))
# print()
# for i in range(len(adj)):
    # print(adj[i])
