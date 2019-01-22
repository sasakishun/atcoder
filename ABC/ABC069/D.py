def listToString(_list, split=""):
    maped_list = map(str, _list)  # mapで要素すべてを文字列に
    mojiretu = split.join(maped_list)
    return mojiretu


h, w = [int(i) for i in input().split()]
n = int(input())
a = [int(i) for i in input().split()]

# 単純に時計回りに配置していけばいいだけ
tile = [[0 for _ in range(w+2)] for _ in range(h+2)]
visited = [[False for _ in range(w+2)] for _ in range(h+2)]
for i in range(len(visited)):
    for j in range(len(visited[0])):
        if i == 0 or i == len(visited)-1 or j == 0 or j == len(visited[0])-1:
            visited[i][j] = True
color = [0 for _ in range(h*w)]
counter = 0
for i in range(len(a)):
    color[counter:counter+a[i]] = [i + 1 for _ in range(a[i])]
    counter += a[i]
# print("color:{}".format(color))
dir = "r" # r, l, u, d
x, y = [1, 1]
while True:
    if len(color) == 0:
        break
    _color = color.pop()
    tile[x][y] = _color
    visited[x][y] = True
    if dir == "r":
        if not visited[x+1][y]:
            x += 1
        else:
            dir = "d"
            y += 1
    elif dir == "d":
        if not visited[x][y+1]:
            y += 1
        else:
            dir = "l"
            x -= 1
    elif dir == "l":
        if not visited[x-1][y]:
            x -= 1
        else:
            dir = "u"
            y -= 1
    elif dir == "u":
        if not visited[x][y-1]:
            y -= 1
        else:
            dir = "r"
            x += 1
for i in range(1, len(tile)-1):
    print(listToString(tile[i][1:-1], " "))