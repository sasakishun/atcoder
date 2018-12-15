n, m = [int(i) for i in input().split()]
table = [0 for _ in range(n)]
for _ in range(m):
    a, b = [int(i) - 1 for i in input().split()]
    table[a] += 1
    table[b] += 1
for _table in table:
    print(_table)