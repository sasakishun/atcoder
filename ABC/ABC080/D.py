def show(imos):
    print(imos[:20])
    print()
n, C = [int(i) for i in input().split()]
imos = [[0 for _ in range(C)] for _ in range(10**5+10)]
for i in range(n):
    s, t, c = [int(i) - 1 for i in input().split()]
    imos[s][c] += 1
    imos[t][c] -= 1
# show(imos)
_max = 0
for i in range(1, len(imos)):
    _count = 0
    for j in range(C):
        if imos[i][j] < 0:
            _count += -imos[i][j]
        imos[i][j] += imos[i-1][j]
    _max = max(_max, sum(imos[i]) + _count)
# show(imos)
print(_max)