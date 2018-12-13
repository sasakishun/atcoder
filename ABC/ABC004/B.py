def listToString(_list, split=""):
    maped_list = map(str, _list)  # mapで要素すべてを文字列に
    mojiretu = split.join(maped_list)
    return mojiretu


c = [[0 for _ in range(4)] for _ in range(4)]
out = [[0 for _ in range(4)] for _ in range(4)]

for i in range(4):
    c[i] = [i for i in input().split()]

#上下反転
for j in range(4):
    out[0][j] = c[3][j]
    out[1][j] = c[2][j]
    out[2][j] = c[1][j]
    out[3][j] = c[0][j]
for i in range(4):
    tmp0 = out[i][0]
    tmp1 = out[i][1]
    out[i][0] = out[i][3]
    out[i][1] = out[i][2]
    out[i][2] = tmp1
    out[i][3] = tmp0
for i in range(4):
    print(listToString(out[i], " "))