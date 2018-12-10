x, y = [int(i) for i in input().split()]
_x = x
# ありうるパターンは
# 符号反転(あり,なし)
# ->インクリメント(負に合わせるのか正に合わせるのか)
# ->符号反転(一意に決定)
# つまり4パターンのみ

count = 10 ** 10
# 符号反転
_x = -x
# 最終反転なし
# インクリメント完全一致
if y >= _x:
    count = min(count, 1 + y - _x)
    # print("count1:{}".format(count))
# 最終反転あり
# インクリメント反転一致
if -y >= _x:
    count = min(count, 1 + (-y) - _x + 1)

# 符号非反転,インクリメント完全一致
_x = x
if y >= _x:
    count = min(count, y - _x)
    # print("count3:{}".format(count))
# インクリメント反転一致
if -y >= _x:
    count = min(count, (-y) - _x + 1)
    # print("count4:{}".format(count))
print(count)