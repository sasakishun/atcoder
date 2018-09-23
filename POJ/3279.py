m = int(input())
n = int(input())

table = [[0 for i in range(n+2)] for j in range(m+2)]

for i in range(1, m+1):
    table[i][1:n+1] = [int(i) for i in input().split()]

count = 0
for i in range(1, m+1):
    for j in range(2, n+1):
        if table[i][j-1] % 2 == 1:
            count += 1
            table[i][j - 1] += 1
            table[i][j + 1] += 1
            table[i - 1][j] += 1
            table[i + 1][j] += 1
for i in range(m+2):
    print(table[i])
print(count)
"""
4
4
1 0 0 1
0 1 1 0
0 1 1 0
1 0 0 1
"""
