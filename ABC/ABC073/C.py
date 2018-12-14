n = int(input())
a = [0 for i in range(n)]
for i in range(n):
    a[i] = int(input())
if n == 1:
    print(1)
    exit()
a = sorted(a)
a.append(-1)  # 番兵を追加
written = []  # 最終的に描かれる数字の集合
counter = 1
# a[0]と同じ数字が途切れた時点でcounterが奇数なら追加する
for i in range(1, len(a)):  # n > 1の場合
    # print()
    # print("a[i]:{} a[i-1]:{} counter:{}".format(a[i], a[i-1], counter))
    if a[i] == a[i - 1]:
        counter += 1
    else:
        if counter % 2 == 1:
            written.append(a[i - 1])
        counter = 1
    # print("a[i]:{} a[i-1]:{} counter:{}".format(a[i], a[i - 1], counter))
print(len(written))
# print(written)
# print(a)