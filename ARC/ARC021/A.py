a = [[0 for _ in range(4)] for _ in range(4)]
for i in range(4):
    a[i] = [int(i) for i in input().split()]

# 左右に滑らせれるか
for i in range(4):
    for j in range(3):
        if a[i][j] == a[i][j + 1]:
            print("CONTINUE")
            exit()
# 上下に滑らせれるか
for j in range(4):
    for i in range(3):
        if a[i][j] == a[i + 1][j]:
            print("CONTINUE")
            exit()
print("GAMEOVER")
