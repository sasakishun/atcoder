adj = [[0 for _ in range(4)] for _ in range(4)]
for i in range(3):
    a, b = [int(i) - 1 for i in input().split()]
    adj[a][b] = 1
    adj[b][a] = 1
for i in range(4):
    for j in range(4):
        if i == j:
            continue
        for k in range(4):
            if i == k or j == k:
                continue
            for l in range(4):
                if i == l or j == l or k == l:
                    continue
                elif adj[i][j] == 1 and adj[j][k] == 1 and adj[k][l] == 1:
                    print("YES")
                    exit()
print("NO")