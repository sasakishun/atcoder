x1, y1, r = [int(i) for i in input().split()]
x2, y2, x3, y3 = [int(i) for i in input().split()]


# つまり片方がもう片方を
# 全てのみ込まなければよい
def dis(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


# 四角が丸を飲み込むとき,赤色無し
if y3 >= y1 + r and y2 <= y1 - r and x2 < x1 - r and x3 >= x1 + r:
    print("NO")
else:
    print("YES")
# 丸が四角を飲み込むとき,青色無し
if dis([x1, y1], [x2, y2]) <= r ** 2 and dis([x1, y1], [x2, y3]) <= r ** 2 and dis([x1, y1],
                                                                                   [x3, y2]) <= r ** 2 and dis([x1, y1],
                                                                                                               [x3,
                                                                                                                y3]) <= r ** 2:
    print("NO")
else:
    print("YES")
