n, m, q = [int(i) for i in input().split()]
imos = [[0 for r in range(n+1)] for l in range(n+1)]
for i in range(m):
    l, r = [int(i) - 1 for i in input().split()]
    imos[0][r] += 1
    imos[l+1][r] -= 1
#imos法
for l in range(n):
    for r in range(1, n):
        imos[l][r] += imos[l][r-1]
for r in range(n):
    for l in range(1, n):
        imos[l][r] += imos[l-1][r]
for i in range(q):
    l, r = [int(i) - 1 for i in input().split()]
    print(imos[l][r])