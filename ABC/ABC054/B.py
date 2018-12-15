n, m = [int(i) for i in input().split()]
a = ["" for _ in range(n)]
b = ["" for _ in range(m)]
for i in range(n):
    a[i] = input()
for i in range(m):
    b[i] = input()
for i in range(n - m + 1):
    for j in range(n - m + 1):
        # bの左上が(i, j)の場合
        match = True
        for k in range(m):
            # print("i:{} j:{} k:{}".format(i, j, k))
            # print(b[k])
            # print(a[i+k][j:j+m])
            # print()
            if b[k] != a[i+k][j:j+m]:
                match = False
                break
        if match:
            print("Yes")
            exit()
print("No")