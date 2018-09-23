n, m, s, t = [int(i) for i in input().split()]
s -= 1
t -= 1
u = [0 for i in range(m)]
v = [0 for i in range(m)]
a = [0 for i in range(m)]
b = [0 for i in range(m)]
before = [[0 for i in range(n)] for j in range(n)]
after = [[0 for i in range(n)] for j in range(n)]

for i in range(m):
    u[i], v[i], a[i], b[i] = [int(i) for i in input().split()]
    u[i] -= 1
    v[i] -= 1
    print("{}:{}".format(u[i], v[i]))
    before[u[i]][v[i]] = a[i]
    after[u[i]][v[i]] = b[i]

while 1:
    for i in range(len(before(u[s]))):