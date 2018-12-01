h, w, t = [int(i) for i in input().split()]
adj = [[0 for i in range(w)] for j in range(h)]
for i in range(h):
    _adj = input()
    for j in range(len(_adj)):
        adj[i][j] = _adj[j]
for i in range(len(adj)):
    print(adj[i])
# 要するに

