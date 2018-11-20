def listToString(_list, split=""):
    maped_list = map(str, _list)  # mapで要素すべてを文字列に
    mojiretu = split.join(maped_list)
    return mojiretu


def stringToList(_string, split=" "):
    str_list = []
    temp = ''
    for x in _string:
        if x == split:  # 区切り文字
            str_list.append(temp)
            temp = ''
        else:
            temp += x
    if temp != '':  # 最後に残った文字列を末尾要素としてリストに追加
        str_list.append(temp)
    return str_list


s = input()
t = input()
firstMatch = False
out = listToString(["z" for i in range(len(s))])
# tがiからスタートするとして全探索O(n^2)<=50*50
for i in range(len(s) - len(t) + 1):
    localStr = []
    match = True
    for j in range(i):  # i番目まではsの?をaで置き換えるだけ
        if s[j] == "?":
            localStr.append("a")
        else:
            localStr.append(s[j])
    for j in range(i, i+len(t)):
        # print("i:{} j:{}".format(i, j))
        # print("s[j]:{} t[j-i]:{}".format(s[j], t[j-i]))
        if s[j] != t[j - i]:
            if s[j] == "?":
                localStr.append(t[j - i])
            else:
                match = False
                break
        else:
            localStr.append(s[j])
    for j in range(i+len(t), len(s)):
        if s[j] == "?":
            localStr.append("a")
        else:
            localStr.append(s[j])
    # print("match:{}".format(match))
    if match:
        firstMatch = True
        if listToString(localStr) < out:
            # print("local:{} out:{}".format(localStr, out))
            out = listToString(localStr)
if firstMatch:
    print(out)
else:
    print("UNRESTORABLE")
