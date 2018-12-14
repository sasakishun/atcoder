def listToString(_list, split=""):
    maped_list = map(str, _list)  # mapで要素すべてを文字列に
    mojiretu = split.join(maped_list)
    return mojiretu

n = int(input())
s = [[0 for _ in range(n)] for _ in range(n)]
for i in range(len(s)):
    s[i] = input()

_s = [[0 for _ in range(n)] for _ in range(n)]
for i in range(len(s)):
    for j in range(len(s)):
        _s[j][n - i - 1] = s[i][j]

for i in range(len(s)):
    print(listToString(_s[i]))