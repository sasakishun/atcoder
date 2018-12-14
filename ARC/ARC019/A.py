def listToString(_list, split=""):
    maped_list = map(str, _list)  # mapで要素すべてを文字列に
    mojiretu = split.join(maped_list)
    return mojiretu


_s = input()
s = ""
for i in range(len(_s)):
    if _s[i] == "O" or _s[i] == "D":
        s += "0"
    elif _s[i] == "I":
        s += "1"
    elif _s[i] == "Z":
        s += "2"
    elif _s[i] == "S":
        s += "5"
    elif _s[i] == "B":
        s += "8"
    else:
        s += _s[i]
print(listToString(s))