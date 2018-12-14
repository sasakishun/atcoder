def listToString(_list, split=""):
    maped_list = map(str, _list)  # mapで要素すべてを文字列に
    mojiretu = split.join(maped_list)
    return mojiretu


s = input()
out = []
for i in range(len(s)):
    if s[i] == "0":
        out.append("0")
    elif s[i] == "1":
        out.append("1")
    else:
        if len(out) > 0:
            out.pop()
print(listToString(out))