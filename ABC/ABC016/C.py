n, m = [int(i) for i in input().split()]
a = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    A, B = [int(i) - 1 for i in input().split()]
    a[A][B] = 1
    a[B][A] = 1
for i in range(n):
    count = [0 for _ in range(n)]
    for j in range(n):
        for k in range(n):
            if i != j and j != k and k != i and a[i][j] == 1 and a[j][k] == 1 and a[k][i] == 0:
                count[k] = 1
                # print("count i:{} j:{} k:{}".format(i+1, j+1, k+1))
    print(sum(count))