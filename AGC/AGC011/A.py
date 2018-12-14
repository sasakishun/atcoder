n, c, k = [int(i) for i in input().split()]
# 合計n人,バス容量c人,到着後k以内に乗る
t = [0 for _ in range(n)]
first = 0  # バス待ちの先頭人の到着時刻
num = 0  # バス待ちの人の数
bass = 0
for i in range(n):
    # 乗客iが到着する時刻
    t[i] = int(input())
t = sorted(t)
for i in range(n):
    # 乗客iが到着する時刻
    if num == 0:
        first = t[i]
        num += 1
    elif first + k < t[i]:
        # print("timeup t:{}".format(t[i]))
        bass += 1
        first = t[i]
        num = 1
    elif num == c:
        # print("over people t:{}".format(t[i]))
        bass += 1
        first = t[i]
        num = 1
    else:
        num += 1
print(bass + 1)
# 必要なバスの台数を出力
# 単純に到着がc人になるか,
# 先頭の人が到着してからk秒たったらバスを出す
