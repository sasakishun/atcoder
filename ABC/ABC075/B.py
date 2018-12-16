def listToString(_list, split=""):
    maped_list = map(str, _list)  # mapで要素すべてを文字列に
    mojiretu = split.join(maped_list)
    return mojiretu


h, w = [int(i) for i in input().split()]
s = [[0 for _ in range(w + 2)] for _ in range(h + 2)]
table = [[0 for _ in range(w + 2)] for _ in range(h + 2)]

for i in range(h):
    _s = input()
    s[i + 1][1:1+w] = [_s[i] for i in range(len(_s))]

for i in range(1, h + 1):
    for j in range(1, w + 1):
        if s[i][j] == "#":
            table[i + 1][j - 1] += 1
            table[i + 1][j] += 1
            table[i + 1][j + 1] += 1
            table[i][j + 1] += 1
            table[i][j - 1] += 1
            table[i - 1][j - 1] += 1
            table[i - 1][j] += 1
            table[i - 1][j + 1] += 1
for i in range(1, h + 1):
    for j in range(1, w + 1):
        if s[i][j] == "#":
            table[i][j] = "#"
for i in range(1, h + 1):
    print(listToString(table[i][1:w+1]))
