def listToString(_list, split=""):
    maped_list = map(str, _list)  # mapで要素すべてを文字列に
    mojiretu = split.join(maped_list)
    return mojiretu


n, l = [int(i) for i in input().split()]
s = ["" for _ in range(n)]
for i in range(len(s)):
    s[i] = input()
s.sort()
print(listToString(s))