n, m, q = [int(i) for i in input().split()]
m_list = [[0 for i in range(n + 1)] for j in range(n + 1)]
dynamic = [[0 for i in range(n + 1)] for j in range(n + 1)]

for i in range(m):
    l, r = [int(i) for i in input().split()]
    m_list[l][r] += 1

for j in range(1, n + 1):
    dynamic[1][j] = dynamic[1][j - 1]
    for k in range(1, j + 1):
        dynamic[1][j] += m_list[k][j]

for i in range(2, n + 1):
    for j in range(i, n + 1):
        if i == j:
            dynamic[i][j] = m_list[i][j]
        else:
            dynamic[i][j] = \
                dynamic[i - 1][j] - \
                dynamic[i - 1][j - 1] - \
                m_list[i - 1][j]

for i in range(q):
    l, r = [int(i) for i in input().split()]
    print(dynamic[l][r])
