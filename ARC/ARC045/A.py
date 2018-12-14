def listToString(_list, split=""):
    maped_list = map(str, _list)  # mapで要素すべてを文字列に
    mojiretu = split.join(maped_list)
    return mojiretu


a = [i for i in input().split()]
# print(a)
out = []
for _a in a:
    if _a == "Left":
        out.append("<")
    elif _a == "Right":
        out.append(">")
    elif _a == "AtCoder":
        out.append("A")
print(listToString(out, " "))