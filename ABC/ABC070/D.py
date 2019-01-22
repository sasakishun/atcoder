n = int(input())
# [[[ノード1, 距離3],[ノード3, 距離5]],[],...]
tree = [[] for _ in range(n+10)]
visited = [-1 for _ in range(n+10)]
# abc = [[0, 0, 0] for _ in range(n)]
for i in range(n-1):
    a, b, c = [int(j) for j in input().split()]
    tree[a - 1].append([b - 1, c])
    tree[b - 1].append([a - 1, c])
q, k = [int(i) for i in input().split()]

stack = [[k-1, 0]]
while True:
    size = len(stack)
    if size == 0:
        break
    now, cost = stack.pop()
    visited[now] = cost
    for i in range(len(tree[now])):
        if visited[tree[now][i][0]] == -1:
            stack.append([tree[now][i][0],
                          cost+tree[now][i][1]])

for _ in range(q):
    x, y = [int(i) - 1 for i in input().split()]
    print(visited[x] + visited[y])