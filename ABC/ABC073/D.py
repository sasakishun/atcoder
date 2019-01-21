import itertools
n, m, R = map(int, input().split())
r = list(map(int, input().split()))
dis = [[float("inf") for _ in range(n)] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    dis[a - 1][b - 1] = c
    dis[b - 1][a - 1] = c

def war(dis):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dis[i][j] > dis[i][k] + dis[k][j]:
                    dis[i][j] = dis[i][k] + dis[k][j]
    return dis
dis = war(dis)
_min = float("inf")
it = itertools.permutations(r)
for iterR in it:
    _dis = 0
    start = iterR[0] - 1
    for end in iterR[1:]:
        _dis += dis[start][end - 1]
        start = end - 1
    _min = min(_min, _dis)
print(_min)
