def listToString(_list, split=""):
    maped_list = map(str, _list)  # mapで要素すべてを文字列に
    mojiretu = split.join(maped_list)
    return mojiretu


_s = input()
s = []
for i in range(len(_s)):
    s.append(_s[i])
n = int(input())
for _ in range(n):
    l, r = [int(i) - 1 for i in input().split()]
    s[l:r + 1] = list(reversed(s[l:r + 1]))
print(listToString(s))
