# 入力「edges:隣接行列」「num_v:頂点数」「start:始点」
def shortest_path(edges, num_v, start):
    inf = float("inf")
    dist = [inf for _ in range(num_v)]
    dist[start] = 0
    # 辺の緩和
    for i in range(num_v):
        for edge in edges:
            if dist[edge[0]] != inf and dist[edge[1]] > dist[edge[0]] + edge[2]:
                dist[edge[1]] = dist[edge[0]] + edge[2]
                if i == num_v - 1 and edge[1] == num_v - 1:
                    print("inf")
                    exit()
    return dist

n, m = [int(i) for i in input().split()]
edges = []
for _ in range(m):
    a, b, c = [int(i) for i in input().split()]
    edges.append([a-1, b-1, -c])
out = shortest_path(edges,n,0)
print(-out[-1])
