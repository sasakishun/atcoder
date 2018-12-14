def listToString(_list, split=""):
    maped_list = map(str, _list)  # mapで要素すべてを文字列に
    mojiretu = split.join(maped_list)
    return mojiretu


s = input()
count = [0 for _ in range(6)]
for _s in s:
    count[ord(_s) - ord("A")] += 1
print(listToString(count, " "))