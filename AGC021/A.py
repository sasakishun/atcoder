def listToString(_list, split=""):
    maped_list = map(str, _list)  # mapで要素すべてを文字列に
    mojiretu = split.join(maped_list)
    return mojiretu


n = int(input())
a = [int(i) for i in str(n)]
count = 0
for i in range(len(str(n))):
    # 下i桁目までで各位の和が最大になるものを算出
    now = a[-i-1:n]
    nowSum = 0
    for j in range(len(now)):
        nowSum += now[j]
    # abcdの時、4桁での最大値はa+(bcdのmax)かa-1 + 9 + 9 + 9
    if a[-i-1] > 0:
        if nowSum < now[0] + 9 * (len(now)-1):
            a[-i-1] -= 1
            for k in range(1, len(now)):
                a[-i-1 + k] = 9
    # print("i:{} a:{} now:{} nowSum:{}".format(i, listToString(a), listToString(now), nowSum))
nowSum = 0
for i in range(len(a)):
    nowSum += a[i]
print(nowSum)