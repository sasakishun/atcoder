n, k = [int(i) for i in input().split()]
a = [[0, 0] for i in range(n)]
for i in range(n):
    a[i][0], a[i][1] = [int(i) for i in input().split()]
a = sorted(a)
sum = 0
for i in range(n):
    sum += a[i][1]
    if sum >= k:
        print(a[i][0])
        exit()
